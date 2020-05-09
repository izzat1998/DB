from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from serializer import serialize

from Person.models import Person
from stats.models import Statistics
from stats.serializers import StatisticsSerializer


class StatisticsApiView(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer


class DataApiView(APIView):
    def get(self, request, **kwargs):
        stats = Statistics.objects.filter(person_id=self.kwargs['person_id'])
        person = Person.objects.get(id=self.kwargs['person_id'])

        walking_list = []
        smoking_list = []
        alcohol_list = []
        dates_list = []

        walking_list.append(stats.values_list('walking_meters_per_day', flat=True))
        smoking_list.append(stats.values_list('avg_num_of_cigarettes_per_day', flat=True))
        alcohol_list.append(stats.values_list('avg_amount_of_alcohol_per_day', flat=True))
        dates_list.append(stats.values_list('date', flat=True))
        response = [{'person_id': self.kwargs['person_id'], 'username': person.username, 'walking': w, 'smoking': s, 'alcohol': a, 'dates': d} for
                    w, s, a, d in zip(walking_list, smoking_list, alcohol_list, dates_list)]

        return Response(response)
