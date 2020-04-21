from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Transpose, SmartResize

# Create your models here.


class News(models.Model):
    """
    abstract class that describe  post's author
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    content = models.TextField(blank=True, verbose_name='контент')
    created = models.DateTimeField(auto_now_add=True, verbose_name='створено')

    class Meta:
        abstract = True


class Category(models.Model):
    """
    model for category for posts
    """
    category = models.CharField(max_length=100, verbose_name='категорія')

    def __str__(self):
        return '{}'.format(self.category)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Article(News):
    """
    model that describe post
    """
    title = models.CharField(max_length=125, verbose_name='Заголовок')
    description = models.CharField(max_length=250, verbose_name='Короткий опис')
    image = models.ImageField(upload_to='article/', null=True, blank=True, verbose_name='фото')
    image_avatar = ImageSpecField(source='image',
                                  processors=[Transpose(), SmartResize(370, 215)],
                                  format='JPEG',
                                  options={'quality': 60})
    image_grid = ImageSpecField(source='image',
                                processors=[Transpose(), SmartResize(370, 304)],
                                format='JPEG',
                                options={'quality': 60})
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name='Категорія')
    is_approve = models.BooleanField(default=False)

    def __str__(self):
        return '"{}" {}'.format(self.title, self.author)

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'


class Reply(News):
    """
    model for reply for post
    """
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return "{}".format(self.author)

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'


class Quote(models.Model):
    """
    simple class for quote
    """
    content = models.CharField(max_length=250, verbose_name='цитата')
    author = models.CharField(max_length=125, verbose_name='автор')

    def __str__(self):
        return '{}'.format(self.author)

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитати'


class Notice(News):
    """
    model for notice, is_flash -show in modal
    """
    title = models.CharField(max_length=125, verbose_name='заголовок')
    is_flash = models.BooleanField(default=False, verbose_name='блискавка')

    class Meta:
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'



