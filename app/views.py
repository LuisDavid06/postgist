from django.shortcuts import render
from rest_framework import viewsets
from app.serializers import serializers
from rest_framework_gis.filters import InBBoxFilter
from app.models import *

# Create your views here.
class LocationViewset(viewsets.ModelViewSet):
    queryset = MainTb002Zone.objects.all()
    serializer_class = serializers.Zone
    bbox_filter_field = 'location'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True # Optional