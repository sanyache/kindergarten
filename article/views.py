from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from .models import *
from .forms import ArticleCreateForm
from event.utils import paginate
# Create your views here.


class ArticleList(ListView):
    """
    class for rendering article list
    """
    model = Article
    queryset = Article.objects.filter(is_approve=True).exclude(category__category='Фінансова звітність')
    template_name = 'blog-grid.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleList, self).get_context_data( object_list=None, **kwargs)
        queryset = self.get_queryset()
        context = paginate(queryset, 3, self.request, context, var_name='articles')
        return context


class ArticleDetail(DetailView):
    """
    class for rendering article by <pk>
    """
    model = Article
    template_name = 'blog-details.html'
    context_object_name = 'article'


class ArticleFinanceList(ListView):
    """
    class for rendering article from finance category
    """
    model = Article
    queryset = Article.objects.filter(category__category='Фінансова звітність')
    template_name = 'blog-grid.html'
    context_object_name = 'articles'


class ArticleCreate(CreateView):
    """
    class for creating article
    """
    model = Article
    form_class = ArticleCreateForm
    template_name = 'blog_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoticeList(ListView):
    """
    class for rendering notice list
    """
    model = Notice
    queryset = Notice.objects.all().order_by('-created')
    template_name = 'notice_list.html'
    context_object_name = 'notices'
