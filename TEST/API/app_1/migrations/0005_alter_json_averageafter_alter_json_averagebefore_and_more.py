# Generated by Django 5.1 on 2024-08-29 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0004_alter_json_datasize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='json',
            name='averageafter',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='json',
            name='averagebefore',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='json',
            name='datasize',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='json',
            name='rawdata',
            field=models.TextField(),
        ),
    ]
