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


class AddressCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    region = serializers.CharField()
    city = serializers.CharField()
    district = serializers.CharField()
    street = serializers.CharField()
    building = serializers.CharField()

    def create(self, validated_data):
        name = validated_data.pop('name')
        region_id = validated_data.pop('region')
        city_id = validated_data.pop('city')
        district_id = validated_data.pop('district')
        street_id = validated_data.pop('street')
        building_id = validated_data.pop('building')
            ############HHHHHHHHH##############
        region = Region.objects.get(id=region_id)
        city = City.objects.get(id=city_id)
        district = District.objects.get(id=district_id)
        street = Street.objects.get(id=street_id)
        building = Building.objects.get(id=building_id)

        address = Address.objects.create(region=region, city=city, district=district, street=street, building=building,
                                         name=name)
        print(address)
        return address


class PersonSerializer(serializers.ModelSerializer):
    diseases = DiseaseSerializer(many=True)
    habits = HabitSerializer(many=True)
    healths = HealthSerializer(many=True)
    address = AddressSerializer()

    class Meta:
        model = Person
        fields = ['id', 'name', 'username', 'phone_number', 'diseases', 'habits', 'healths', 'address']
