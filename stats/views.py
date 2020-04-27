from django.shortcuts import render
from rest_framework import viewsets

from stats.models import Statistics
from stats.serializers import StatisticsSerializer


class StatisticsApiView(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
