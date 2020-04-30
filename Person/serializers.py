from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import serializers

from Person.models import Person, Habit, Health, Disease, Address, Region, City, District, Street, Building


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'name']


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = ['id', 'name']


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['id', 'name']


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ['id', 'name']


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class BuildingSerializerForAddress(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ['id', 'name']


class StreetSerializerForAddress(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ['id', 'name']


class DistrictSerializerForAddress(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name']


class CitySerializerForAddress(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class RegionSerializerForAddress(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', ]


class AddressSerializer(serializers.ModelSerializer):
    region = RegionSerializerForAddress()
    city = CitySerializerForAddress()
    district = DistrictSerializerForAddress()
    street = StreetSerializerForAddress()
    building = BuildingSerializerForAddress()

    class Meta:
        model = Address
        fields = ['id', 'name', 'region', 'city', 'district', 'street', 'building']


class PersonSerializer(serializers.ModelSerializer):
    disease = DiseaseSerializer(many=True)
    habit = HabitSerializer(many=True)
    health = HealthSerializer(many=True)
    address = AddressSerializer()

    class Meta:
        model = Person
        fields = ['id', 'name', 'username', 'user_type', 'phone_number', 'disease', 'habit', 'health', 'address']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

