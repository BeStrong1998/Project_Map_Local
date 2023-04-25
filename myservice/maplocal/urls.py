from django.urls import path, include
from rest_framework import routers
from . import views



router = routers.DefaultRouter()
router.register(r'citys', views.CityViewSet)
router.register(r'streets', views.StreetViewSet)
router.register(r'markets', views.MarketViewSet)

urlpatterns = [
    #path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]


