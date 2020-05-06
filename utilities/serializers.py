from rest_framework import serializers
from .models import *

class HospitalIPDSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalIpdPatient
        fields = ['user_id', 'name', 'listing_id']