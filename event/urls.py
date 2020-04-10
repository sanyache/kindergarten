from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('event_list', EventList.as_view(), name='event_list'),
    path('event_deatils/<int:pk>', EventDetail.as_view(), name='event_details'),
    path('gallery', GalleryList.as_view(), name='gallery_list'),
    path('image_gallery/<int:pk>', image_gallery, name='gallery_detail')
]