from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kioskVacansyController import views


router = DefaultRouter()
router.register(r"districts", views.DistrictsViewSet, basename="districts")


urlpatterns = [
    path("", include(router.urls))
]
