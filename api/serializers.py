from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'category', 'name', 'price',)
