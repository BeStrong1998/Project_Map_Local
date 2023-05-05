from rest_framework import viewsets
from .serializers import CitySerializer, StreetSerializer, MarketSerializer
from .models import City, Street, Market
# from rest_framework.response import Response
from rest_framework.decorators import action


class CitysViewSet(viewsets.ModelViewSet):          # колекция городов
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetsViewSet(viewsets.ModelViewSet):        # колекция улиц
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class GetStreetsViewSet(viewsets.ModelViewSet):     # колекция улиц
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    @action(detail=True, methods=['get'])
    def get_queryset(self):
        queryset = Street.objects.all()
        city_id = self.kwargs['city_id']
        if city_id is not None:
            queryset = queryset.filter(city_id=city_id)
        return queryset


class MarketsViewSet(viewsets.ModelViewSet):        # колекция магазинов
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
