from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Event, Gallery, ImageGallery, CategoryGallery

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


class ImageGalleryInLine(admin.TabularInline):
    """
    for show foreign key dependence
    """
    model = ImageGallery
    fields = ('image',)
    extra = 0


@admin.register(CategoryGallery)
class CategoryGalleryAdmin(admin.ModelAdmin):
    """
    class for model CategoryGallery
    """
    list_display = ('name',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """
    class for model Gallery
    """

    model = Gallery
    list_display = ('title', 'created')
    inlines = [ImageGalleryInLine]


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    """
    class for model ImageGallery
    """

    model = ImageGallery
    list_display = ('get_gallery',)

    def get_gallery(self, obj):
        return obj.gallery.title



