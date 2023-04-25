from django.db import models

# Create your models here.


class City(models.Model):
    city = models.CharField(max_length=30)

    def __repr__(self):
        return self.city


class Street(models.Model):
    street = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __repr__(self):
        return self.street


class Market(models.Model):
    name = models.CharField(max_length=30)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    house = models.IntegerField(default=0)
    time_opening = models.DateTimeField()
    time_closeding = models.DateTimeField()

    def __repr__(self):
        return self.name