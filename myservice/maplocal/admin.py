from django.contrib import admin

from .models import City, Street, Market

admin.site.register(City)
admin.site.register(Street)
admin.site.register(Market)

# Register your models here.
