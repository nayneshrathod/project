from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class RetrievePatientListView(generics.GenericAPIView):
    def post(self,request):
        objects_to_return = HospitalIpdPatient.objects.filter(sex__icontains="female")
        serializer = HospitalIPDSerializer(objects_to_return, many=True)
        return JsonResponse({"patient_list":serializer.data})
