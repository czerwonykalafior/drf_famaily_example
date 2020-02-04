from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'families', views.FamilyViewSet)
router.register(r'papas', views.PapaViewSet)
router.register(r'mamas', views.MamaViewSet)
router.register(r'kids', views.KidViewSet)
router.register(r'toys', views.ToyViewSet)
router.register(r'toy-owners', views.ToyOwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
