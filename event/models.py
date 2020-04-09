from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose, SmartResize
# Create your models here.


class Gallery(models.Model):
    """
    class  describe Gallery
    """
    title = models.CharField(max_length=125, verbose_name='назва альбому')
    title_image = models.ImageField(upload_to='title/', verbose_name='титульне фото')
    description = models.CharField(max_length=250, blank=True, verbose_name='опис альбому')
    created = models.DateField(auto_now_add=True, verbose_name='створено')

    def __str__(self):
        return "{}".format(self.title)


class ImageGallery(models.Model):
    """
    class describe photo for gallery
    """
    image = models.ImageField(upload_to='gallery/%Y/%m/%d', verbose_name='фото')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='галерея',
                                related_name='gallery_image')


class Event(models.Model):
    """
    class for describe event at kindergarten
    """
    title = models.CharField(max_length=125, verbose_name='назва події')
    title_image = models.ImageField(upload_to='event_title/%Y/%m/%d', blank=True, null=True,
                                    verbose_name='фото обложки')
    title_image_avatar = ImageSpecField(source='title_image',
                                        processors=[Transpose(),SmartResize(370, 300)],
                                        format='JPEG',
                                        options={'quality':60})
    title_image_detail = ImageSpecField(source='title_image',
                                        processors=[Transpose(), SmartResize(870, 469)],
                                        format='JPEG',
                                        options={'quality': 80})
    created = models.DateField(auto_now_add=True, verbose_name='створено')
    scheduled = models.DateTimeField(blank=True, null=True, verbose_name='дата проведення')
    description = models.CharField(max_length=250, verbose_name='опис')
    place = models.CharField(max_length= 200, blank=True, verbose_name='місце проведення')
    content = models.TextField(blank=True, verbose_name='контент')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='gallery_event', verbose_name='галерея')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.title)
