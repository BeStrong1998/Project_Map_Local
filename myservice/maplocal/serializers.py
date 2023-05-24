from rest_framework import serializers

from .models import City, Street, Market


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'city')


class StreetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Street
        fields = ('id', 'street', 'city')


class MarketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Market
        fields = ('id', 'name', 'street', 'city', 'house', 'time_opening', 'time_closeding')
