from django.conf.urls import url
from rest_framework import routers
from api.views import FlightViewSet
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'flights', FlightViewSet)

schema_view = get_swagger_view(title='API Docs')

urlpatterns = [
    url(r'^docs/', schema_view)
]

urlpatterns += router.get_urls()
