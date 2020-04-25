from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Person.models import Person, Habit, Disease, Health, Address, Region, City, District, Street, Building
from Person.serializers import PersonSerializer, HealthSerializer, HabitSerializer, DiseaseSerializer, \
    AddressSerializer, CitySerializer, RegionSerializer, DistrictSerializer, StreetSerializer, BuildingSerializer


class PeopleApiView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DiseaseApiView(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class HabitApiView(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HealthApiView(viewsets.ModelViewSet):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer


class AddressApiView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class RegionApiView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer



class CityApiView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class DistrictApiView(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class StreetApiView(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class BuildingApiView(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
