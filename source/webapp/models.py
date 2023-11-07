from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')
    parent_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
