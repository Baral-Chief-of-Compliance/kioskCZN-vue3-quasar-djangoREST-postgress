from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kioskController import views


router = DefaultRouter()
router.register(r"departments", views.DepartmentViewSet, basename="department")
router.register(r"events", views.EventViewSet, basename="event")
router.register(r"floors", views.FloorViewSet, basename="floor")
router.register(r"games", views.GameViewSet, basename="game")
router.register(r"info_materials", views.InfoMaterialsViewSet, basename="info_material")
router.register(r"personal_centers", views.PCViewSet, basename="personal_center")
router.register(r"posts", views.PostViewSet, basename="post")
router.register(r"rooms", views.RoomViewSet, basename="room")
router.register(r"services", views.ServiceViewSet, basename="serivce")
router.register(r"workers", views.WorkerViewSet, basename="worker")
router.register(r"workers_in_departments", views.WorkerInDepartmentViewSet, basename="workers_in_departments")


urlpatterns = [
    path("", include(router.urls))
]
