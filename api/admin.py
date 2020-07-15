from django.contrib import admin
from .models import Item, Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class ItemAdmin(admin.ModelAdmin):
    # リストに作成日を追加
    list_display = ('category', 'name',  'price', 'created_at')
    # リンクををカテゴリーと名前に設定
    list_display_links = ('category', 'name')
    # フィリターにカテゴリーを追加
    list_filter = ('category',)
    # 検索項目に名前を設定
    search_fields = ('name',)


admin.site.register(Item, ItemAdmin)

admin.site.register(Category, CategoryAdmin)
