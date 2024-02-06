# Generated by Django 4.2.7 on 2024-02-05 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Заголовок')),
                ('floor', models.PositiveSmallIntegerField(verbose_name='Этаж')),
                ('max_floor', models.PositiveSmallIntegerField(verbose_name='Этажей в доме')),
                ('description', models.TextField(verbose_name='Описание')),
                ('square', models.PositiveIntegerField(verbose_name='Площадь')),
                ('price', models.PositiveIntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Обьект недвижимости',
                'verbose_name_plural': 'Обьекты недвижимости',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Количество комнат')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Описание комнат')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='TypeRealty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Тип недвижимости')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Описание типа')),
            ],
            options={
                'verbose_name': 'Тип жилья',
                'verbose_name_plural': 'Типы жилья',
            },
        ),
        migrations.CreateModel(
            name='TypeTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, unique=True, verbose_name='Тип сделки')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Описание сделки')),
            ],
            options={
                'verbose_name': 'Сделка',
                'verbose_name_plural': 'Сделки',
            },
        ),
        migrations.CreateModel(
            name='RealtyPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='realty/', verbose_name='Изображение')),
                ('realty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.realty', verbose_name='Жилье')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.AddField(
            model_name='realty',
            name='_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realty.typerealty'),
        ),
        migrations.AddField(
            model_name='realty',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='realty',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realty.rooms'),
        ),
        migrations.AddField(
            model_name='realty',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realty.typetransaction'),
        ),
    ]