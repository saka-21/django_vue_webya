from django.db import models

# Categoryモデルの作成


class Category (models.Model):
    # ラベル付け
    class Meta:
        verbose_name = "商品カテゴリー"
        verbose_name_plural = "商品カテゴリー"

    name = models.CharField('カテゴリー名', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # このモデルのデフォルト返却値にnameを設定
    def __str__(self):
        return self.name


class Item (models.Model):
    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"

    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    # category = models.IntegerField('カテゴリー')　←コメントアウト
    # 新たにcategoryという名前でCategoryモデルへのアソシエーション作成
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('商品名', max_length=255)
    description = models.TextField('詳細', max_length=1000)
    price = models.IntegerField('金額')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
