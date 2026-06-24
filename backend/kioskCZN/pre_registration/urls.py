from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pre_registration import views


router = DefaultRouter()
router.register(r"", views.PreRegistrationViewSet, basename="queues")

urlpatterns = [
    path("", include(router.urls))
]
