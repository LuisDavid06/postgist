from app.models import * 
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class Zone(GeoFeatureModelSerializer):
    
    class Meta:
        model = MainTb002Zone
        geo_field = 'geometry'
        bbox_geo_field = 'bbox_geometry'
        auto_bbox = True
        fields  = ('id', 'zone')

        
