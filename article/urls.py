from django.urls import path
from django.contrib.auth.decorators import permission_required
from .views import *

urlpatterns = [
    path('article_list', ArticleList.as_view(), name='article_list'),
    path('article_detail/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('article_create', permission_required('is_staff')(ArticleCreate.as_view()), name='article_create'),
    path('finance', ArticleFinanceList.as_view(), name='finance'),
    path('notice_list', NoticeList.as_view(), name='notice_list'),
]