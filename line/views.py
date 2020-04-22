from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import PersonInLine
from .forms import PersonInLineForm
from event.utils import paginate
# Create your views here.


class PersonInLineCreate(CreateView):
    """
    view for creating person in line
    """
    model = PersonInLine
    form_class = PersonInLineForm
    template_name = 'line_create.html'
    success_url = reverse_lazy('index')


class LineList(ListView):

    model = PersonInLine
    queryset = PersonInLine.objects.filter(is_approve=True).order_by('wish_year',
                                                                     'group_age',
                                                                     '-privilege',
                                                                     'created')
    template_name = 'line.html'
    context_object_name = 'lines'

    def get_queryset(self):
        queryset = super(LineList, self).get_queryset()
        if self.request.GET.get('wish_year'):
            year = int(self.request.GET.get('wish_year'))
            queryset = queryset.filter(wish_year=year)
        if self.request.GET.get('group_age'):
            age = int(self.request.GET.get('group_age'))
            queryset = queryset.filter(group_age=age)
        if self.request.GET.get('last_name'):
            last_name = self.request.GET.get('last_name')
            queryset = queryset.filter(child_last_name=last_name)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LineList, self).get_context_data( object_list=None, **kwargs)
        queryset = self.get_queryset()
        context = paginate(queryset, 20, self.request, context, var_name='lines')
        return context
