from rest_framework import serializers

from flight.models import Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('id', 'flight_number', 'city_start', 'city_end',
                  'airplane', 'start_time', 'fact_time', 'status')
