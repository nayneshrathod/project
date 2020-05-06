from rest_framework import serializers
from .models import ObstetricForm, ObstetricPhysicalExamination


class ObstetricFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObstetricForm
        fields = "__all__"


class PhysicalExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObstetricPhysicalExamination
        fields = "__all__"
