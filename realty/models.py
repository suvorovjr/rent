from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class TypeRealty(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Тип недвижимости')
    description = models.CharField(max_length=150, verbose_name='Описание типа', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип жилья'
        verbose_name_plural = 'Типы жилья'


class TypeTransaction(models.Model):
    transaction = models.CharField(max_length=50, unique=True, verbose_name='Тип сделки')
    description = models.CharField(max_length=150, verbose_name='Описание сделки', **NULLABLE)

    def __str__(self):
        return self.transaction

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'


class Rooms(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='Количество комнат')
    description = models.CharField(max_length=150, verbose_name='Описание комнат', **NULLABLE)

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Realty(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    realty_type = models.ForeignKey(TypeRealty, on_delete=models.SET_NULL, **NULLABLE)
    transaction = models.ForeignKey(TypeTransaction, on_delete=models.SET_NULL, **NULLABLE)
    room = models.ForeignKey(Rooms, on_delete=models.SET_NULL, **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='Заголовок', **NULLABLE)
    floor = models.PositiveSmallIntegerField(verbose_name='Этаж')
    max_floor = models.PositiveSmallIntegerField(verbose_name='Этажей в доме')
    description = models.TextField(verbose_name='Описание')
    square = models.PositiveIntegerField(verbose_name='Площадь')
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    publish = models.BooleanField(default=False, verbose_name='Активность')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            (
                'set_published',
                'Can publish posts'
            )
        ]
        verbose_name = 'Обьект недвижимости'
        verbose_name_plural = 'Обьекты недвижимости'


class RealtyPhoto(models.Model):
    realty = models.ForeignKey(Realty, related_name='photo', on_delete=models.CASCADE, verbose_name='Жилье')
    photo = models.ImageField(upload_to='realty/', verbose_name='Изображение', **NULLABLE)

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
