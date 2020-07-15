from rest_framework import viewsets
from django.shortcuts import render
from django.views import generic
from .serializers import ItemSerializer
from .models import Item


class ItemViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer


# class IndexView(generic.TemplateView):
#     template_name = 'index.html'


# def find_all(request):
#     data = Item.objects.all()
#     params = {
#         'data': data
#     }
#     return render(request, 'all.html', params)
