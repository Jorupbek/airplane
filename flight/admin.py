# -*- coding: utf-8 -*-
from django.contrib import admin
from flight.models import Flight, Airplane, City


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'city_start', 'city_end', 'airplane',
                    'start_time', 'fact_time', 'status')
    list_display_links = ('flight_number', 'city_start', 'city_end',
                          'airplane', 'start_time', 'fact_time')
    list_editable = ['status']
    list_filter = ['flight_number', 'city_start', 'city_end', 'status',
                   'start_time']


@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'airport_name')
