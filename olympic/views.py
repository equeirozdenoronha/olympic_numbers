from olympic.models import NOC, Athlete
from olympic.serializers import NOCSerializer, AthleteSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


class DefaultPagination(LimitOffsetPagination):
    default_limit = 80
    max_page_size = 350


class NocViewSet(viewsets.ModelViewSet):
    queryset = NOC.objects.all()
    serializer_class = NOCSerializer
    pagination_class = DefaultPagination
    lookup_field = 'noc'
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_fields = ('noc', 'country_name')
    search_fields = ('noc', 'country_name')


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    pagination_class = DefaultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_fields = ('name', 'sex', 'age', 'team', 'sport')
    search_fields = ('name', 'sex', 'age', 'team', 'sport')