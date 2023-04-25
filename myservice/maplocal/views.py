#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import viewsets

from .serializers import CitySerializer, StreetSerializer, MarketSerializer
from .models import City, Street, Market



"""def index(request):
    return HttpResponse("Hello, world!")"""

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('city')
    serializer_class = CitySerializer


class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all().order_by('street')
    serializer_class = StreetSerializer


class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all().order_by('name')
    serializer_class = MarketSerializer