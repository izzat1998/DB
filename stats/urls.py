from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from stats.views import StatisticsApiView

router = routers.DefaultRouter()
router.register('stats', StatisticsApiView)

urlpatterns = [
    path('', include(router.urls))
]
