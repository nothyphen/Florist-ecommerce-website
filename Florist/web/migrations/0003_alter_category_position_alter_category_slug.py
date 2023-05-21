# Generated by Django 4.2.1 on 2023-05-21 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_category_position_category_slug_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='position',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
