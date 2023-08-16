# Generated by Django 4.1.3 on 2022-11-05 18:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlledBridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель управляемого моста',
                'verbose_name_plural': 'Модели управляемых мостов',
            },
        ),
        migrations.CreateModel(
            name='DrivingBridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель ведущего моста',
                'verbose_name_plural': 'Модели ведущих мостов',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель двигателя',
                'verbose_name_plural': 'Модели двигателей',
            },
        ),
        migrations.CreateModel(
            name='Technic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель техники',
                'verbose_name_plural': 'Модели техники',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель трансмиссии',
                'verbose_name_plural': 'Модели трансмиссий',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=12, unique=True, verbose_name='Зав. № машины')),
                ('engine_number', models.CharField(max_length=12, verbose_name='Зав. № двигателя')),
                ('transmission_number', models.CharField(max_length=12, verbose_name='Зав. № трансмиссии')),
                ('driving_bridge_number', models.CharField(max_length=12, verbose_name='Зав. № ведущего моста')),
                ('controlled_bridge_number', models.CharField(max_length=12, verbose_name='Зав. № управляемого моста')),
                ('delivery_contract', models.CharField(max_length=20, verbose_name='Договор поставки №, дата')),
                ('date_shipment', models.DateField(default=datetime.datetime.now, verbose_name='Дата отгрузки с завода')),
                ('сonsignee', models.CharField(max_length=200, verbose_name='Грузополучатель (конечный потребитель)')),
                ('delivery_address', models.CharField(max_length=200, verbose_name='Адрес поставки (эксплуатации)')),
                ('equipment', models.TextField(verbose_name='Комплектация (доп. опции)')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('controlled_bridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.controlledbridge', verbose_name='Модель управляемого моста')),
                ('driving_bridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.drivingbridge', verbose_name='Модель ведущего моста')),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.engine', verbose_name='Модель двигателя')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicecompany', verbose_name='Сервисная компания')),
                ('technic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.technic', verbose_name='Модель техники')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.transmission', verbose_name='Модель трансмиссии')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
    ]
