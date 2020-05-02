from django.contrib import admin
from django.urls import path, include

from Person.views import PeopleApiView, HabitApiView, DiseaseApiView, HealthApiView, AddressApiView, RegionApiView, \
    CityApiView, DistrictApiView, StreetApiView, BuildingApiView, PersonLoginApiView
from rest_framework import routers

from stats.views import StatisticsApiView

router = routers.DefaultRouter()
router.register('people', PeopleApiView)
router.register('health', HealthApiView)
router.register('disease', DiseaseApiView)
router.register('habit', HabitApiView)
router.register('address', AddressApiView)
router.register('region', RegionApiView)
router.register('city', CityApiView)
router.register('district', DistrictApiView)
router.register('street', StreetApiView)
router.register('building', BuildingApiView)
router.register('statistic', StatisticsApiView)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', PersonLoginApiView.as_view(), name='login')
]
