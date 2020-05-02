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

from Person.models import Person, Habit, Disease, Health, Address, Region, City, District, Street, Building
from Person.serializers import PersonSerializer, HealthSerializer, HabitSerializer, DiseaseSerializer, \
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


            # qs = qs.filter(address__region=region, address__city=city, address__district=district, address__street=street,
            #                address__building=building, habit=habit, disease=disease)

        # qs = qs.filter(
        #         Q(disease__name__icontains=query) | Q(habit__name__icontains=query) | Q(
        #             health__name__icontains=query) | Q(address__region__name__icontains=query) | Q(
        #             address__city__name__icontains=query) | Q(address__district__name__icontains=query) | Q(
        #             address__street__name__icontains=query) | Q(address__building__name__icontains=query))
        return qs

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        username = request.data['username']
        email = request.data['email']
        gender = request.data['gender']
        phone_number = request.data['phone_number']
        region = request.data['region']
        city = request.data['city']
        district = request.data['district']
        street = request.data['street']
        building = request.data['building']
        healths_id = request.data['healths']
        diseases_id = request.data['diseases']
        habits_id = request.data['habits']
        password = request.data['password']
        a = Address.objects.create(region_id=region, city_id=city, district_id=district, street_id=street, building_id=building)
        address_id = a.id
        person = Person.objects.create(name=name, username=username, password=password, phone_number=phone_number,
                                       address_id=address_id, email=email, gender=gender)
        person.disease.add(*diseases_id)
        person.health.add(*healths_id)
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
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials!'})
        person = Person.objects.get(username=username, password=password)
        return Response({'user_id': user.id,
                         'username': user.username,
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


class HealthApiView(viewsets.ModelViewSet):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer

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
