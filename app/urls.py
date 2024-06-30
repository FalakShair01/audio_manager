from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AudioClipViewset

router = DefaultRouter()
router.register(r'audio', AudioClipViewset)

urlpatterns = [
    path('', include(router.urls))
]