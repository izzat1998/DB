from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from stats.views import StatisticsApiView, DataApiView

router = routers.DefaultRouter()
router.register('', StatisticsApiView)
# router.register('data', DataApiView, basename='data')

urlpatterns = [
    path('data/<int:person_id>/', DataApiView.as_view(), name='data'),
    path('', include(router.urls)),

]
