from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('event_list', EventList.as_view(), name='event_list'),
    path('event_deatils/<int:pk>', EventDetail.as_view(), name='event_details'),
]