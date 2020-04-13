from django.urls import path
from .views import *

urlpatterns = [
    path('about_us/', about_us, name='about_us'),
    path('group_detail/<int:pk>', GroupDetail.as_view(), name='group_detail')
]