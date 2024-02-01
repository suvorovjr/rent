from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, unique=True, verbose_name='Слаг')
    body = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Превью', **NULLABLE)
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
