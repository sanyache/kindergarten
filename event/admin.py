from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Event, Gallery, ImageGallery

# Register your models here.


class EventAdminForm(forms.ModelForm):
    """
    form for event model with ckeditor
    """
    content = forms.CharField(label="контент", widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = Event
        fields = '__all__'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    model = Event
    list_display = ('title', 'scheduled', 'is_active')
    ordering = ['scheduled']
    form = EventAdminForm


