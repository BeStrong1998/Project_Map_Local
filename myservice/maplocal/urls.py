from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CitysViewSet, GetStreetsViewSet, MarketsViewSet


router = routers.DefaultRouter()
router.register(r'citys', views.CitysViewSet)       # Коллекция citys
router.register(r'streets', views.StreetsViewSet)   # коллекция streets
router.register(r'markets', views.MarketsViewSet)   # коллекция markets

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('city/<int:pk>/', CitysViewSet.as_view({'get': 'retrieve'})),
    path('city/<int:city_id>/street/', GetStreetsViewSet.as_view({'get': 'list'})),
    path('market/street=city/', MarketsViewSet.as_view({'get': 'list'})),
]


# path('market/', MarketsViewSet.as_view({'post': 'update'})),