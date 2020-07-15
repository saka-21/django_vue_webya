from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'category', 'name', 'price',)

# ↓ここから追加


class SearchItemFilter(filters.FilterSet):
    # name項目に対してcontains=部分一致で検索する。
    name = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Item
        fields = ('category',)
