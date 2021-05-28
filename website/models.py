from django.db import models


class Authors(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Фамилия')
    login = models.CharField(max_length=100, null=False, blank=False, verbose_name='Логин')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')

    def __str__(self):
        return self.name


# Модель Category содержит название тега; Может не Category а Tag???
class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    published = models.BooleanField(verbose_name='Опубликован')
    author = models.ForeignKey(Authors, null=True, on_delete=models.SET_NULL, verbose_name='Автор')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='Категории')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')

    def __str__(self):
        return self.title
