from django.urls import path, include
from rest_framework.routers import DefaultRouter

from yandexApiKeys import views


router = DefaultRouter()
router.register(r"active", views.ActiveYandexAPIKeyList, basename="active-yandex-api-key")

urlpatterns = [
    path("", include(router.urls))
]