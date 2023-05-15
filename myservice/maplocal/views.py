from datetime import datetime
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

    @action(detail=True, methods=['get'])
    def get_queryset(self):
        # print(self.request.query_params)
        queryset = Market.objects.all()
        city_name = self.request.query_params.get('city')
        if city_name is not None:
            queryset = queryset.filter(city_name=city_name)

        street_name = self.request.query_params.get('street')
        if street_name is not None:
            queryset = queryset.filter(street_name=street_name)


        return queryset
