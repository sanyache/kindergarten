from django.contrib import admin
from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.


class ArticleAdminForm(forms.ModelForm):
    """
    form for article model with ckeditor
    """
    content = forms.CharField(label="контент", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Article
        fields = '__all__'


class ReplyInLine(admin.TabularInline):

    model = Reply
    fields = ('author', 'content')
    extra = 0


class ArticleAdmin(admin.ModelAdmin):

    model = Article
    list_display = ('author', 'get_category', 'title', 'is_approve', 'created')
    list_display_links = ('author', 'title')
    list_filter = ('author', 'is_approve', 'get_category')
    list_filter = ('author', 'is_approve', 'category')
    form = ArticleAdminForm
    inlines = [ReplyInLine]

    def get_category(self, obj):
        return obj.category.category


class CategoryAdmin(admin.ModelAdmin):

    model = Category
    list_display = ('category',)


class ReplyAdmin(admin.ModelAdmin):

    model = Reply
    list_display = ('author', 'created')


class QuoteAdmin(admin.ModelAdmin):

    model = Quote


admin.site.register(Article, ArticleAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Quote, QuoteAdmin)