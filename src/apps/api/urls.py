from django.urls import path
from rest_framework.routers import SimpleRouter

from .viewsets.vps import VPSViewSet

app_name = "api"

router = SimpleRouter()

router.register("vps", VPSViewSet, basename="vps")

urlpatterns = router.urls