from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Person.models import Person, Habit, Disease, Health, Address, Region, City, District, Street, Building
from Person.serializers import PersonSerializer, HealthSerializer, HabitSerializer, DiseaseSerializer, \
    AddressSerializer, CitySerializer, RegionSerializer, DistrictSerializer, StreetSerializer, BuildingSerializer


class PeopleApiView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        username = request.data['username']
        phone_number = request.data['phone_number']
        address_id = request.data['address']
        healths_id = request.data['healths']
        diseases_id = request.data['diseases']
        habits_id = request.data['habits']
        person = Person.objects.create(name=name, username=username, phone_number=phone_number, address_id=address_id)
        person.disease.add(*diseases_id)
        person.health.add(*healths_id)
        person.habit.add(*habits_id)
        person.save()
        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data, safe=False)


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

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        region_id = request.data['region']
        city_id = request.data['city']
        district_id = request.data['district']
        street_id = request.data['street']
        building_id = request.data['building']
        address = Address.objects.create(region_id=region_id, city_id=city_id, district_id=district_id,
                                         street_id=street_id, building_id=building_id,
                                         name=name)
        serializer = AddressSerializer(address)
        return JsonResponse(serializer.data, safe=False)


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
