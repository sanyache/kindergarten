from django.urls import path
from .views import *

urlpatterns = [
    path('article_list', ArticleList.as_view(), name='article_list'),
    path('article_detail/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('finance', ArticleFinanceList.as_view(), name='finance'),
]