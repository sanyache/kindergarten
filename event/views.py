from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import *
from .utils import paginate
# Create your views here.


def index(request):

    events = Event.objects.all().order_by('-scheduled')[:3]

    return render(request, 'index.html', {'events': events})


class EventList(ListView):
    """
    view for rendering event list
    """
    model = Event
    template_name = 'event-grid.html'
    queryset = Event.objects.all()

    def get_queryset(self):
        queryset = super(EventList, self).get_queryset()
        queryset.filter(scheduled__lt=timezone.now()).update(is_active=False)
        return queryset.order_by('-scheduled')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventList, self).get_context_data( object_list=None, **kwargs)
        queryset = self.get_queryset()
        context = paginate(queryset, 3, self.request, context, var_name='events')
        return context


class EventDetail(DetailView):
    """
    view for rendering event details
    """
    model = Event
    template_name = 'event-details.html'
    context_object_name = 'event'
