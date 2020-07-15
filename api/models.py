from django.db import models

# Create your models here.


class Item(models.Model):
    category = models.IntegerField('カテゴリー')
    name = models.CharField(max_length=255)
    description = models.TextField('商品名', max_length=255)
    price = models.IntegerField('金額')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
