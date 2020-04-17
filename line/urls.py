from django.urls import path
from .views import *

urlpatterns = [
    path('create_inline', PersonInLineCreate.as_view(), name='create_inline'),
    path('line', LineList.as_view(), name='line')
]