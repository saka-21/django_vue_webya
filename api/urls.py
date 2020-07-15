from django.urls import path
from . import views
from rest_framework import routers
from .views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'category', ItemViewSet)
urlpatterns = router.urls

# app_name = 'api'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('all/', views.find_all, name='all')
# ]
