from django.contrib import admin

# Register your models here.
from Person.models import Person, Health, Habit, Disease, Address, Region, City, District, Building, Street


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    pass

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    pass

@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(District)
class DistrcitAdmin(admin.ModelAdmin):
    pass

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    pass

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    pass