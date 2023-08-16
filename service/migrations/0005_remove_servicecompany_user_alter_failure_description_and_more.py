# Generated by Django 4.1.3 on 2022-11-06 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_servicecompany_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecompany',
            name='user',
        ),
        migrations.AlterField(
            model_name='failure',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='recoverymethod',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='servicecompany',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='typemaintenance',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]