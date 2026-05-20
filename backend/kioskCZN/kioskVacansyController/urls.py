from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kioskVacansyController import views


router = DefaultRouter()
router.register(r"districts", views.DistrictsViewSet, basename="districts")
router.register(r"vacancies", views.VacansyViewSet, basename="vacancies")
router.register(r"user_from_max_mini_app", views.UserFromMaxMiniAppViewSet, basename="user_from_max_mini_app")
router.register(r"favorite_vacancies", views.FavoriteVacansyViewSet, basename="favorite_vacancies")


urlpatterns = [
    path("", include(router.urls))
]
