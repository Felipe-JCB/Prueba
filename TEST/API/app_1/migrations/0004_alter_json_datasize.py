# Generated by Django 5.1 on 2024-08-29 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_rename_cantidad_max_json_averageafter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='json',
            name='datasize',
            field=models.IntegerField(),
        ),
    ]
