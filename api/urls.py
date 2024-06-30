from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ModelViewSet, VersionViewSet, MetadataViewSet, PerformanceViewSet, StatusViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'models', ModelViewSet)
router.register(r'versions', VersionViewSet)
router.register(r'metadata', MetadataViewSet)
router.register(r'performance', PerformanceViewSet)
router.register(r'status', StatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]