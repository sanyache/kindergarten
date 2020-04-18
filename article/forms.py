from django import forms
from .models import Article
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleCreateForm(forms.ModelForm):
    """
    form for creating article
    """
    content = forms.CharField(widget=CKEditorUploadingWidget, label='Контент')


    class Meta:
        model = Article
        exclude = ('is_approve', 'author')
