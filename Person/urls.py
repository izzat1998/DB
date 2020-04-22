from django.contrib import admin
from django.urls import path, include

from Person.views import PeopleList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('people', PeopleList)
urlpatterns = [
    path('', include(router.urls))
]
