# from django.urls import path
# from . import views
from rest_framework import routers
from .views import ItemViewSet, SearchItemViewSet

router = routers.DefaultRouter()
router.register(r'category', ItemViewSet)
router.register(r'item', SearchItemViewSet)
urlpatterns = router.urls
