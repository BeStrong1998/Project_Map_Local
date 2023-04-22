from django.db import models

# Create your models here.


class City(models.Model):
    city = models.CharField(max_length=30)


class Street(models.Model):
    street = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Market(models.Model):
    name = models.CharField(max_length=30)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    house = models.IntegerField()
    time_opening = models.DateTimeField(auto_now_add=True)
    time_closeding = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name