from django.urls import path, include
from rest_framework import routers
from . import views
from .views import *



router = routers.DefaultRouter()
router.register(r'citys', views.CitysViewSet) #Коллекция citys
router.register(r'streets', views.StreetsViewSet) #коллекция streets
router.register(r'markets', views.MarketsViewSet) #коллекция markets

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('city/', CityViewSet.as_view()),  #Колекция объекта город
    path('city/<int:pk>/', CityDetail.as_view()), #один бъект из колекции по id
    path('city/create/', CityCreateView.as_view()), #для создания нового объекта
    path('city/<int:city_id>/street/', StreetViewset.as_view()), #все улицы одного города
    path('street/create/', StreetCreateView.as_view()), #для создания улиц
    path('market/', MarketViewSet.as_view()), #Колекция объекта магазин
    path('market/create/', MarketCreateView.as_view()), #для создания магазинов
]


