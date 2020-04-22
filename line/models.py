import datetime
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from kindergarten.settings import ADMIN_EMAIL

# Create your models here.


class PersonInLine(models.Model):
    """
    class describe child, parent in queue
    """
    YEAR_CHOICES = [(r,r) for r in range(datetime.date.today().year, datetime.date.today().year+7)]
    PRIVILEGE_CHOICES = (
        (3, 'діти воїнів АТО'),
        (2, 'діти інваліди'),
        (1, 'діти з багатодітних сімей'),
        (0, 'на загальних засадах')
    )
    GROUP_AGE_CHOICES = (
        (1, 'молодша'),
        (2, 'середня'),
        (3, 'старша')
    )
    child_last_name = models.CharField(max_length=50, verbose_name="Прізвище дитини")
    child_first_name = models.CharField(max_length=30, verbose_name="Ім'я дитини")
    child_middle_name = models.CharField(max_length=30, verbose_name="По-батькові")
    child_birthday = models.DateField(verbose_name='день народження')
    birth_certificate = models.CharField(max_length=15,
                                         verbose_name='Свідоцтво про народження',
                                         )
    certificate_issued = models.CharField(max_length=125, verbose_name='Ким видане')
    address = models.CharField(max_length=200, verbose_name='адреса')
    wish_year = models.IntegerField(choices=YEAR_CHOICES, default=0, verbose_name='Рік зарахування')
    parent_last_name = models.CharField(max_length=50, verbose_name="Прізвище батька")
    parent_first_name = models.CharField(max_length=30, verbose_name="Ім'я батька")
    parent_middle_name = models.CharField(max_length=30, verbose_name="По-батькові")
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    privilege = models.PositiveSmallIntegerField(choices=PRIVILEGE_CHOICES, verbose_name='пільга')
    created = models.DateField(auto_now_add=True, verbose_name='створено')
    group_age = models.PositiveSmallIntegerField(choices=GROUP_AGE_CHOICES,
                                                 verbose_name='вікова група')
    is_approve = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Дитина в черзі'
        verbose_name_plural = 'Черга'


@receiver(post_save, sender=PersonInLine)
def person_inline_post_save(sender, instance, created, **kwargs):
    if created:
        send_mail('Реєстрація в електронній черзі',
                  'Подано заяву на реєстрацію від {} {} від {}'.format(instance.parent_last_name,
                                                                       instance.parent_first_name,
                                                                       instance.created),
                  ADMIN_EMAIL,
                  [ADMIN_EMAIL, ' ulia41475@gmail.com'])
        send_mail('Реєстрація в електронній черзі',
                  'Ваша заява до електронної черги прийнята, після перевірки даних ваш запис буде '
                  'розміщено в електронній черзі. Дату реєстрації {} збережено і вона не залежитиме'
                  'від дати розміщення в черзі'.format(instance.created),
                  ADMIN_EMAIL,
                  [instance.email],)

