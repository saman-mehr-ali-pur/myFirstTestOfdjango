from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quickstart.views import *

router = DefaultRouter()
router.register(r'passngerView', PassngerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]