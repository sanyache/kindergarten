# Generated by Django 2.0.1 on 2020-04-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=125)),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Стаття', 'verbose_name_plural': 'Статті'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name': 'Коментар', 'verbose_name_plural': 'Коментарі'},
        ),
    ]