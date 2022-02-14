from rest_framework import viewsets, permissions
from flight.models import Flight
from api.serializers import FlightSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

