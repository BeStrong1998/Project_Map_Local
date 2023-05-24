from datetime import datetime
from rest_framework import viewsets
from .serializers import CitySerializer, StreetSerializer, MarketSerializer
from .models import City, Street, Market
# from rest_framework.response import Response
from rest_framework.decorators import action
from functools import reduce
from django.db.models import Q
from django.http import HttpResponse


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
        print(self.request.query_params)
        queryset = Market.objects.all()
        # queryset = Market.objects.filter()
        city_name = self.request.query_params.get('city', None)
        if city_name is not None:
            queryset = queryset.filter(city=city_name)

        street_name = self.request.query_params.get('street', None)
        if street_name is not None:
            queryset = queryset.filter(street=street_name)

        open = self.request.query_params.get('open', None)
        if open is not None:
            tim = datetime.now().time().hour
            open_market = queryset.filter(time_opening__hour__lte=tim).filter(
                time_closeding__hour__gte=tim)
            if open == '1':
                queryset = open_market
            elif open == '0':
                queryset = queryset.exclude(id__in=open_market) # исключаем результат из open_market

        return queryset