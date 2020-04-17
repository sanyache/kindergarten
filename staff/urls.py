from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('about_us/', about_us, name='about_us'),
    path('group_detail/<int:pk>', GroupDetail.as_view(), name='group_detail'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
]