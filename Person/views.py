from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from Person.models import Person, Habit, Disease, Address, Region, City, District, Street, Building
from Person.serializers import PersonSerializer, HabitSerializer, DiseaseSerializer, \
    AddressSerializer, CitySerializer, RegionSerializer, DistrictSerializer, StreetSerializer, BuildingSerializer, \
    UserLoginSerializer


class PeopleApiView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        qs = Person.objects.all()
        region = self.request.GET.get('region_id')
        city = self.request.GET.get('city_id')
        district = self.request.GET.get('district_id')
        street = self.request.GET.get('street_id')
        building = self.request.GET.get('building_id')
        habit = self.request.GET.get('habit_id')
        disease = self.request.GET.get('disease_id')

        if region is not None:
            qs = qs.filter(address__region=region)
        if city is not None:
            qs = qs.filter(address__city=city)
        if district is not None:
            qs = qs.filter(address__district=district)
        if street is not None:
            qs = qs.filter(address__street=street)
        if building is not None:
            qs = qs.filter(address__building=building)
        if habit is not None:
            qs = qs.filter(habit=habit)
        if disease is not None:
            qs = qs.filter(disease=disease)

        return qs

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        username = request.data.get('username')
        email = request.data.get('email')
        gender = request.data.get('gender')
        phone_number = request.data.get('phone_number')
        region = request.data.get('region')
        city = request.data.get('city')
        district = request.data.get('district')
        street = request.data.get('street')
        building = request.data.get('building')
        diseases_id = request.data.getlist('diseases')
        habits_id = request.data.getlist('habits')
        password = request.data.get('password')
        user_type = request.data.get('user_type')
        a = Address.objects.create(region_id=int(region), city_id=int(city), district_id=int(district), street_id=int(street), building_id=int(building))
        address_id = a.id
        person = Person.objects.create(name=name, username=username, password=password, phone_number=phone_number,
                                       address_id=address_id, email=email, gender=gender, user_type=user_type)
        if diseases_id:
            person.disease.add(*diseases_id)
        if habits_id:
            person.habit.add(*habits_id)
        person.save()
        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data, safe=False)


class PersonLoginApiView(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password!'})
        # user = authenticate(username=username, password=password)
        # if not user:
        #     return Response({'error': 'Invalid credentials!'})
        person = Person.objects.get(username=username, password=password)
        return Response({'user_id': person.id,
                         'username': person.username,
                         'user_type': person.user_type})


class DiseaseApiView(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

    # def get_queryset(self):
    #     qs = Disease.objects.all()
    #     query = self.request.GET.get()
    #     if query is not None:
    #         qs = qs.filter()
    #     return qs


class HabitApiView(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    # def get_queryset(self):
    #     qs = Disease.objects.all()
    #     query = self.request.GET.get()
    #     if query is not None:
    #         qs = qs.filter()
    #     return qs


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

    def get_queryset(self):
        qs = Address.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(region__name__icontains=query) | Q(city__name__icontains=query) | Q(
                    district__name__icontains=query) | Q(street__name__icontains=query) | Q(
                    building__name__icontains=query))
        return qs


class RegionApiView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CityApiView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        qs = City.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(region__name__icontains=query))
        return qs


class DistrictApiView(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def get_queryset(self):
        qs = District.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(city__name__icontains=query))
        return qs


class StreetApiView(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    def get_queryset(self):
        qs = Street.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(district__name__icontains=query))
        return qs


class BuildingApiView(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def get_queryset(self):
        qs = Building.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(street__name__icontains=query))
        return qs
