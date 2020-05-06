import json

from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination


class MTPListViewPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class MTPCreateView(generics.CreateAPIView):
    queryset = MedicalTerminationOfPregnancyRecord.objects.all()
    serializer_class = MTPSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        print(response.data)
        return JsonResponse({
            'status': 200,
            'message': 'success',
            'mtp_record': response.data
        })


class MTPCreateViewNew(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        print(type(json_object))
        mtp_record = json_object.get("mtp_record")
        print("HIT",json_object)
        if not mtp_record:
            return JsonResponse({"status":400, "message":"Bad Request", "error":"KeyError : Key 'mtp_record' missing"})
        serializer = MTPNewSerializer(data=mtp_record)
        if serializer.is_valid():
            print("SERIALIZER VALID")
            serializer.save()
            return JsonResponse({"status": 201, "message": "Created", "mtp_record": serializer.data})
        else:
            return JsonResponse({"status": 400, "message": "Bad Request", "mtp_record": serializer.errors})


class MTPUpdateView(generics.GenericAPIView):
    # queryset = MedicalTerminationOfPregnancyRecord.objects.all()
    # serializer_class = MTPSerializer
    #
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return JsonResponse({
    #         "status": 200,
    #         "message": "success",
    #         "updated_mtp_record": serializer.data
    #     })
    def post(self, request):
        json_body = json.loads(request.body)
        json_object = json_body.get("mtp_record", None)
        if not json_object:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"MTP data is required"})
        hospital_id = json_object.get("hospital_id", None)
        id = json_object.get("id", None)

        if hospital_id:
            hospital_id = int(hospital_id)
        else:
            return JsonResponse({"status": 400, "message": "Bad Request", "data": "Please provide required fields"})
        if id:
            id = int(id)
        else:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"Please provide required fields"})

        if MedicalTerminationOfPregnancyRecord.objects.filter(id=id).exists():
            mtp_object = MedicalTerminationOfPregnancyRecord.objects.get(id=id)
            if hospital_id != mtp_object.hospital_id:
                return JsonResponse({"status":400, "message":"Bad Request", "data":"patient does not exist at your hospital"})
            mtp_object.date_of_admission = json_object.get("date_of_admission", mtp_object.date_of_admission)
            mtp_object.phone = json_object.get("phone", mtp_object.phone)
            mtp_object.name_of_patient = json_object.get("name_of_patient", mtp_object.name_of_patient)
            mtp_object.contact_name = json_object.get("contact_name", mtp_object.contact_name)
            mtp_object.age = json_object.get("age", mtp_object.age)
            mtp_object.weight = json_object.get("weight", mtp_object.weight)
            mtp_object.duration_of_pregnancy = json_object.get("duration_of_pregnancy", mtp_object.duration_of_pregnancy)
            mtp_object.reason_of_termination = json_object.get("reason_of_termination", mtp_object.reason_of_termination)
            mtp_object.type_of_abortion = json_object.get("type_of_abortion", mtp_object.type_of_abortion)
            mtp_object.date_of_termination = json_object.get("date_of_termination", mtp_object.date_of_termination)
            mtp_object.date_of_discharge = json_object.get("date_of_discharge", mtp_object.date_of_discharge)
            mtp_object.results_and_remarks = json_object.get("results_and_remarks", mtp_object.results_and_remarks)
            mtp_object.treatment_given = json_object.get("treatment_given", mtp_object.treatment_given)
            mtp_object.post_abortion_complication_identified = json_object.get("post_abortion_complication_identified", mtp_object.post_abortion_complication_identified)
            mtp_object.post_abortion_complication_treated = json_object.get("post_abortion_complication_treated", mtp_object.post_abortion_complication_treated)
            mtp_object.save()
            mtp_object = MedicalTerminationOfPregnancyRecord.objects.get(id=id)
            serializer = MTPReadSerializer(mtp_object)
            return JsonResponse({"status": 200, "message": "success", "mtp_record": serializer.data})
        else:
            return JsonResponse({"status": 400, "message": "Bad Request"})



class MTPRetrieveView(generics.GenericAPIView):
    # def post(self, request):
    #     object_mtp = MedicalTerminationOfPregnancyRecord.objects.get(pk=kwargs['pk'])
    # queryset = MedicalTerminationOfPregnancyRecord.objects.all()
    # serializer_class = MTPReadSerializer

    #
    # #    def retrieve(self, request, *args, **kwargs):
    # #        self.object = self.get_object()
    # #        serializer = self.get_serializer(self.object)
    # #        return HttpResponse(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     serializer = self.get_serializer(self.object)
    #     print("MTPRetrieveAPIView response :", serializer.data)
    #     # return Response(serializer.data)
    #     return HttpResponse(json.dumps(serializer.data), status=200, content_type='application/json')
    def post(self, request):
        json_object = json.loads(request.body)
        hospital_id = json_object.get("hospital_id", None)
        id = json_object.get("id", None)
        if hospital_id:
            hospital_id = int(hospital_id)
        else:
            return JsonResponse({"status": 400, "message": "Bad Request", "data": "Please provide required fields"})
        if id:
            id = int(id)
        else:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"Please provide required fields"})

        if MedicalTerminationOfPregnancyRecord.objects.filter(id=id, hospital_id=hospital_id).exists():
            mtp_objects = MedicalTerminationOfPregnancyRecord.objects.filter(id=id, hospital_id=hospital_id)
            print(mtp_objects)
            serializer = MTPReadSerializer(mtp_objects, many=True)
            return JsonResponse({"status":200, "message":"Success", "data":serializer.data})
        else:
            return JsonResponse({"status":400, "message":"Bad Request"})


class MTPListView(generics.ListAPIView):
    queryset = MedicalTerminationOfPregnancyRecord.objects.all()
    serializer_class = MTPListSerializer
    # pagination_class = MTPListViewPaginator

    def list(self, request, *args, **kwargs):
        print("\n As requested ", request.method)
        queryset = self.filter_queryset(self.get_queryset())

        #page = self.paginate_queryset(queryset)
        #if page is not None:
        #    serializer = self.get_serializer(page, many=True)
        #    return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset.order_by('-pk'), many=True)
        print("MTPListAPIView response :", serializer.data)
        #return HttpResponse(json.dumps(serializer.data), content_type='application/json')
        return JsonResponse({"status":200,"message":"success", "results":serializer.data})


class MTPDropDownView(generics.GenericAPIView):
    def post(self, request):
        abortion_choices = []
        tuple_list = MedicalTerminationOfPregnancyRecord.ABORTION_CHOICES
        for tuplee in tuple_list:
            (id, valuee) = tuplee
            abortion_choices.append({"id": id, "value": valuee})
        # responsee = json.dumps(abortion_choices)
        return JsonResponse({"abortion_choices": abortion_choices})

class MTPReadByHospital(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        hospital_id = json_object.get("hospital_id", None)
        if not hospital_id:
            return JsonResponse({"status":400, "message":"Bad Request"})
        if MedicalTerminationOfPregnancyRecord.objects.filter(hospital_id=hospital_id).exists():
            mtp_records = MedicalTerminationOfPregnancyRecord.objects.filter(hospital_id=hospital_id)
            serializer  = MTPReadSerializer(mtp_records, many=True)
            return JsonResponse({"status":200, "message":"Success", "data":serializer.data})
        else:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"No such Hospital exists"})


class MTPDeleteView(generics.GenericAPIView):
    def post(self, request):
        #json_body = json.loads(request.body)
        #print(json_body)
        json_object = json.loads(request.body)
        print("JSON OBJECT", json_object)
        if not json_object:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"MTP data is required"})
        hospital_id = json_object.get("hospital_id", None)
        id = json_object.get("id", None)
        if not hospital_id or not id:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"Please provide required fields"})
        id = int(id)
        hospital_id = int(hospital_id)
        if MedicalTerminationOfPregnancyRecord.objects.filter(id=id).exists():
            mtp_object = MedicalTerminationOfPregnancyRecord.objects.get(id=id)
            if hospital_id != mtp_object.hospital_id:
                return JsonResponse({"status":400, "message":"Bad Request", "data":"patient does not exist at your hospital"})
            mtp_object.delete()
            print("OBJECT DELETED")
        return JsonResponse({"status":200, "message":"Success"})



class TestTestClass(generics.GenericAPIView):
    def post(self, request, pk):
        json_object = self.pk  # json.GET.get(params)
        print(json_object)
        return HttpResponse(json_object, status=200)
