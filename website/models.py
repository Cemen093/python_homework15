from django.db import models


class Authors(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Фамилия')
    login = models.CharField(max_length=100, null=False, blank=False, verbose_name='Логин')


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')


# Модель Category содержит название тега; Может не Category а Tag???
class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    published = models.BooleanField(verbose_name='Опубликован')
    author = models.ForeignKey(Authors, null=True, on_delete=models.SET_NULL, verbose_name='Автор')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='Категории')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
