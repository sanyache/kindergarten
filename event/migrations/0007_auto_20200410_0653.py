# Generated by Django 2.0.1 on 2020-04-10 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20200409_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.CategoryGallery'),
        ),
    ]