from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer, SearchItemFilter


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# ↓以下追加


class SearchItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_class = SearchItemFilter
