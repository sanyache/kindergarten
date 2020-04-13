from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Transpose, SmartResize

# Create your models here.


class Staff(models.Model):
    """
    abstract class for staff
    """
    first_name = models.CharField(max_length=125, verbose_name="ім'я")
    last_name = models.CharField(max_length=125, verbose_name='прізвище')
    middle_name = models.CharField(max_length=125, blank=True, verbose_name='по-батькові')
    birthday = models.DateField(verbose_name='день народження')
    image = models.ImageField(upload_to='staff/', verbose_name='фото')
    image_avatar = ImageSpecField(source='image',
                                  processors=[Transpose(), SmartResize(370, 377)],
                                  format='JPEG',
                                  options={'quality': 70})
    image_small = ImageSpecField(source='image',
                                  processors=[Transpose(), SmartResize(164, 136)],
                                  format='JPEG',
                                  options={'quality': 60})
    description = models.TextField(blank=True)
    def get_full_name(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.middle_name)

    class Meta:
        abstract = True


class Tutor(Staff):
    """
    class describe a tutor
    """
    POSITION = (
        ('tutor', 'Вихователь'),
        ('assistant', 'Помічник', ),
        ('psychologist', 'Психолог'),
        ('music', 'Муз керівник'),
        ('sport', 'Фіз рук')
    )
    tutor_position= models.CharField(max_length=15, choices=POSITION, verbose_name='посада')
    education = models.CharField(max_length=250, blank=True, verbose_name='освіта')
    experience = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='стаж роботи')
    qualification = models.CharField(max_length=250, blank=True, verbose_name='кваліфікація')

    def __str__(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.tutor_position)

    class Meta:
        verbose_name = 'Вихователь'
        verbose_name_plural = 'Вихователі'


class Section(models.Model):
    """
    class describe section(class) for studying
    """
    name = models.CharField(max_length=250, verbose_name='гурток')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, verbose_name='керівник',
                              related_name='section_tutor')
    image = models.ImageField(upload_to='section/', blank=True, null=True, verbose_name='фото')
    description = models.TextField(blank=True, null=True, verbose_name='опис')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Гурток'
        verbose_name_plural = 'Гуртки'


class Group(models.Model):
    """
    class describe a group
    """

    AGE = (
        ('L','Старша'),
        ('M', 'Середня'),
        ('S','Молодша')
    )
    name = models.CharField(max_length=125, verbose_name='назва групи')
    image = models.ImageField(upload_to='group/', blank=True, null=True, verbose_name='фото групи')
    image_avatar = ImageSpecField(source='image',
                                  processors=[Transpose(), SmartResize(370, 250)],
                                  format='JPEG',
                                  options={'quality': 70})
    image_big = ImageSpecField(source='image',
                                  processors=[Transpose(), SmartResize(830, 421)],
                                  format='JPEG',
                                  options={'quality': 100})
    age_group = models.CharField(max_length=1, choices=AGE, verbose_name='вікова група')
    tutor = models.ManyToManyField(Tutor, verbose_name='вихователь', related_name='group_tutor')
    section = models.ManyToManyField(Section, related_name='group_section',
                                verbose_name='гурток')
    description = models.CharField(max_length=500, blank=True , verbose_name='опис групи')
    about_us = models.TextField(blank=True, null=True, verbose_name='про нас')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'
