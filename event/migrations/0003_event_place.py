# Generated by Django 2.0.1 on 2020-04-07 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(blank=True, max_length=200, verbose_name='місце проведення'),
        ),
    ]
