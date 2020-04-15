from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import *
from article.models import Article, Quote, Notice
from .utils import paginate
# Create your views here.


def index(request):

    events = Event.objects.all().order_by('-scheduled')[:3]
    galleries = Gallery.objects.all().order_by('-created')[:6]
    articles = Article.objects.filter(is_approve=True).exclude(
                                      category__category='Фінансова звітність').order_by('-created')[:3]
    quotes = Quote.objects.all()
    notice = Notice.objects.filter(is_flash=True).order_by('-created').first()
    return render(request, 'index.html', {'events': events,
                                          'galleries': galleries,
                                          'articles': articles,
                                          'quotes': quotes,
                                          'notice': notice})


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


class GalleryList(ListView):
    """
    view for rendering gallery list
    """
    model = Gallery
    queryset = Gallery.objects.all()
    context_object_name = 'galleries'
    template_name = 'gallery.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GalleryList, self).get_context_data( object_list=None, **kwargs)
        categories = CategoryGallery.objects.all()
        context['categories'] = categories
        return context


def image_gallery(request, pk):
    """
    view for rendering photo gallery
    """
    gallery = get_object_or_404(Gallery, id=pk)
    photos = ImageGallery.objects.filter(gallery=gallery)
    context = paginate(photos, 4, request, {}, var_name='photos')
    context['gallery'] = gallery
    return render(request, 'gallery_detail.html', context)
