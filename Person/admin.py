from django.contrib import admin

# Register your models here.
from Person.models import Person, Health, Habit, Disease


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    pass

@admin.register(Habit)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Health)
class PersonAdmin(admin.ModelAdmin):
    pass