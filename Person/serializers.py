from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import serializers

from Person.models import Person, Habit, Health, Disease, Address, Region, City, District, Street, Building


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class BuildingSerializerForAddress(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class StreetSerializerForAddress(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class DistrictSerializerForAddress(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class CitySerializerForAddress(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class RegionSerializerForAddress(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


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
        fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

