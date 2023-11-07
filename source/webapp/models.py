from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')
    parent_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    user_id = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='articles',
                                verbose_name="Автор")
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Контент")
    image = models.ImageField(null=True, blank=True, upload_to='product_pics', verbose_name='Изображение')

    def __str__(self):
        return f'{self.pk}. {self.title}'
