from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets


from Person.models import Person
from Person.serializers import PersonSerializer


class PeopleList(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

