# Generated by Django 5.1.3 on 2024-11-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketcars', '0002_alter_car_image_alter_car_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='brand_name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='brand_name_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='brand_name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_color_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_color_fr',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_color_ru',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_ru',
            field=models.TextField(null=True),
        ),
    ]