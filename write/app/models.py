from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=255)

    def __str__(self):
        return f"{self.id}. {self.name}"

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category,
                                 related_name='posts',
                                 on_delete=models.CASCADE)
    published_at = models.DateTimeField(
        auto_now_add=True
    )
    is_published = models.BooleanField(default=False)
    list = {
        'private': 'приватный',
        'public': 'публичный'
    }
    status = models.CharField(choices=list, max_length=255)

    def __str__(self):
        return f'{self.id}. {self.title}'

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        ordering = ['id']
