from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return(self.name)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return(self.name)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    mini_text = models.TextField(verbose_name='Краткое содержание')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(verbose_name='Время создания')
    slug = models.SlugField(verbose_name='url', max_length=100)

    def __str__(self):
        return(self.title)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    created_date = models.DateTimeField(verbose_name='Время создания комментария')
    moderation = models.BooleanField(verbose_name='Видимость коммнтария')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Коментарии"
