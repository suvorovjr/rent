from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, unique=True, verbose_name='Слаг', **NULLABLE)
    body = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Превью', **NULLABLE)
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey(Categories, related_name='category', on_delete=models.CASCADE, verbose_name='Категория')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


class Version(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='новость')
    version_number = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Номер версии')
    version_name = models.CharField(max_length=255, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='Текущая версия')

    def __str__(self):
        return f'{self.version_name} - {self.version_number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
