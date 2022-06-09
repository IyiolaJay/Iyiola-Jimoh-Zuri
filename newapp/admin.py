from django.contrib import admin

from .models import Country, School



# Register your models here.
admin.site.register(School)
admin.site.register(Country)