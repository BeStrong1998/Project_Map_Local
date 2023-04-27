from rest_framework import viewsets
from rest_framework import generics
from .serializers import CitySerializer, StreetSerializer, MarketSerializer
from .models import City, Street, Market
from rest_framework.response import Response



"""def index(request):
    return HttpResponse("Hello, world!")"""

class CitysViewSet(viewsets.ModelViewSet): #колекция городов
    queryset = City.objects.all()#.order_by('city')
    serializer_class = CitySerializer


class StreetsViewSet(viewsets.ModelViewSet): #колекция улиц
    queryset = Street.objects.all()#.order_by('street')
    serializer_class = StreetSerializer


class MarketsViewSet(viewsets.ModelViewSet): #колекция магазинов
    queryset = Market.objects.all()#.order_by('name')
    serializer_class = MarketSerializer




class CityViewSet(generics.ListAPIView): #Берём всю коллекцию оюъекта
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def handle(self, ex):
        return Response({'data': 'Коллекция пуста'}, status=400)


class CityDetail(generics.RetrieveAPIView): #Берём один объект из колекции
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def handle(self, ex):
        return Response({'data': 'Нету такого города с указанным city_id'}, status=400)


class CityCreateView(generics.CreateAPIView): #Создаём новый объект
    serializer_class = CitySerializer
    
    def handle(self, ex):
        return Response({'data': 'Добавьте город'}, status=400)
    

class StreetViewset(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        queryset = Street.objects.all()
        city_id = self.kwargs['city_id']
        if city_id is not None:
            queryset = queryset.filter(city_id=city_id)
        return queryset
    

class StreetCreateView(generics.CreateAPIView):
    serializer_class = StreetSerializer

    def handle(self, ex):
        return Response({'data': 'Добавьте улицу'}, status=400)


class MarketCreateView(generics.CreateAPIView):
    serializer_class = MarketSerializer

    def handle(self, ex):
        return Response({'data': 'Добавьте магазин'}, status=400)
    

class MarketViewSet(generics.ListAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
