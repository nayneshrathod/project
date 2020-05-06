from django.http import JsonResponse
from rest_framework import generics
from .models import DeliveryRecord
import json
from .serializers import DeliveryRecordFrontEndSerializer, DeliveryRecordSerializer, DeliveryRecordListSerializer, DeliveryDataFESerializer
from .delivery_serializers import DeliveryRecordReadSerializer, DeliveryRecordReadFinalSerializer



class UpdateDeliveryRecordView(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        delivery = json_object.get("delivery_data")
        id_received = delivery.get('id')
        data = {}
        if DeliveryRecord.objects.filter(id=id_received).exists():
            delivery_obj = DeliveryRecord.objects.get(id=id_received)
            print(delivery_obj)
            apgar = json_object.get("apgar_score")
            #delivery = json_object.get("delivery_data")
            print(apgar)
            apgar_serializer = DeliveryRecordFrontEndSerializer(data=apgar)

            delivery_serializer = DeliveryRecordSerializer(data=delivery)
            if apgar_serializer.is_valid():
                print("INSIDE APGAR SERIALIZER", type(apgar_serializer.validated_data))
                print("INSIDE APGAR SERIALIZER", type(apgar_serializer.data))

                if delivery_serializer.is_valid():
                    print("DELIVERY SERIALIZER VALID")

                    delivery_obj.type_of_delivery = delivery_serializer.data['type_of_delivery'] if delivery_serializer.data['type_of_delivery'] else delivery_obj.type_of_delivery
                    print("YES!!")
                    delivery_obj.sex = delivery_serializer.data['sex'] if delivery_serializer.data['sex'] else delivery_obj.sex
                    delivery_obj.live_birth = delivery_serializer.data["live_birth"] if delivery_serializer.data["live_birth"] else delivery_obj.live_birth
                    delivery_obj.still_birth = delivery_serializer.data["still_birth"] if delivery_serializer.data["still_birth"] else delivery_obj.still_birth
                    delivery_obj.name = delivery_serializer.data["name"] if delivery_serializer.data["name"] else delivery_obj.name
                    delivery_obj.age = delivery_serializer.data["age"] if delivery_serializer.data["age"] else delivery_obj.age
                    delivery_obj.weight = delivery_serializer.data["weight"] if delivery_serializer.data["weight"] else delivery_obj.weight
                    delivery_obj.preterm = delivery_serializer.data["preterm"] if delivery_serializer.data["preterm"] else delivery_obj.preterm
                    delivery_obj.type_of_delivery = delivery_serializer.data['type_of_delivery'] if delivery_serializer.data['type_of_delivery'] else delivery_obj.type_of_delivery
                    delivery_obj.abortion_types = delivery_serializer.data['abortion_types'] if delivery_serializer.data['abortion_types'] else delivery_obj.abortion_types

                    delivery_obj.heart_rate_1_min_value = apgar_serializer.data['heart_rate_1_min_value'] if apgar_serializer.data['heart_rate_1_min_value'] else delivery_obj.heart_rate_1_min_value
                    delivery_obj.heart_rate_1_min_slot = apgar_serializer.data['heart_rate_1_min_slot'] if apgar_serializer.data['heart_rate_1_min_slot'] else delivery_obj.heart_rate_1_min_slot

                    delivery_obj.muscle_tone_1_min_value = apgar_serializer.data['muscle_tone_1_min_value'] if apgar_serializer.data['muscle_tone_1_min_value'] else delivery_obj.muscle_tone_1_min_value
                    delivery_obj.muscle_tone_1_min_slot = apgar_serializer.data['muscle_tone_1_min_slot'] if apgar_serializer.data['muscle_tone_1_min_slot'] else delivery_obj.muscle_tone_1_min_slot

                    delivery_obj.reflex_1_min_value = apgar_serializer.data['reflex_1_min_value'] if apgar_serializer.data['reflex_1_min_value'] else delivery_obj.reflex_1_min_value
                    delivery_obj.reflex_1_min_slot = apgar_serializer.data['reflex_1_min_slot'] if apgar_serializer.data['reflex_1_min_slot'] else delivery_obj.reflex_1_min_slot

                    delivery_obj.colour_1_min_value = apgar_serializer.data['colour_1_min_value'] if apgar_serializer.data['colour_1_min_value'] else delivery_obj.colour_1_min_value
                    delivery_obj.colour_1_min_slot = apgar_serializer.data['colour_1_min_slot'] if apgar_serializer.data['colour_1_min_slot'] else delivery_obj.colour_1_min_slot

                    delivery_obj.respiratory_effort_1_min_value = apgar_serializer.data['respiratory_effort_1_min_value'] if apgar_serializer.data['respiratory_effort_1_min_value'] else delivery_obj.respiratory_effort_1_min_value
                    delivery_obj.respiratory_effort_1_min_slot = apgar_serializer.data['respiratory_effort_1_min_slot'] if apgar_serializer.data['respiratory_effort_1_min_slot'] else delivery_obj.respiratory_effort_1_min_slot

                    delivery_obj.heart_rate_5_min_value = apgar_serializer.data['heart_rate_5_min_value'] if apgar_serializer.data['heart_rate_5_min_value'] else delivery_obj.heart_rate_5_min_value
                    delivery_obj.heart_rate_5_min_slot = apgar_serializer.data['heart_rate_5_min_slot'] if apgar_serializer.data['heart_rate_5_min_slot'] else delivery_obj.heart_rate_5_min_slot

                    delivery_obj.muscle_tone_5_min_value = apgar_serializer.data['muscle_tone_5_min_value'] if apgar_serializer.data['muscle_tone_5_min_value'] else delivery_obj.muscle_tone_5_min_value
                    delivery_obj.muscle_tone_5_min_slot = apgar_serializer.data['muscle_tone_5_min_slot'] if apgar_serializer.data['muscle_tone_5_min_slot'] else delivery_obj.muscle_tone_5_min_slot

                    delivery_obj.reflex_5_min_value = apgar_serializer.data['reflex_5_min_value'] if apgar_serializer.data['reflex_5_min_value'] else delivery_obj.reflex_5_min_value
                    delivery_obj.reflex_5_min_slot = apgar_serializer.data['reflex_5_min_slot'] if apgar_serializer.data['reflex_5_min_slot'] else delivery_obj.reflex_5_min_slot

                    delivery_obj.colour_5_min_value = apgar_serializer.data['colour_5_min_value'] if apgar_serializer.data['colour_5_min_value'] else delivery_obj.colour_5_min_value
                    delivery_obj.colour_5_min_slot = apgar_serializer.data['colour_5_min_slot'] if apgar_serializer.data['colour_5_min_slot'] else delivery_obj.colour_5_min_slot

                    delivery_obj.respiratory_effort_5_min_value = apgar_serializer.data['respiratory_effort_5_min_value'] if apgar_serializer.data['respiratory_effort_5_min_value'] else delivery_obj.respiratory_effort_5_min_value
                    delivery_obj.respiratory_effort_5_min_slot = apgar_serializer.data['respiratory_effort_5_min_slot'] if apgar_serializer.data['respiratory_effort_5_min_slot'] else delivery_obj.respiratory_effort_5_min_slot

                    delivery_obj.save()
                    obj = DeliveryRecord.objects.get(id = delivery_obj.id)
                    print(obj)
                    serializer = DeliveryRecordSerializer(obj)
                    delivery_data_serializer = DeliveryDataFESerializer(obj)
                    data["delivery_data"] = delivery_data_serializer.data
                    final_serializer = DeliveryRecordReadSerializer(data=serializer.data)
                    if final_serializer.is_valid():
                        final_read_serializer = DeliveryRecordReadFinalSerializer(data=final_serializer.data)
                        if final_read_serializer.is_valid():
                            data["apgar_score"] = final_read_serializer.data
                            return JsonResponse({"status":200, "message":"Success", "data":data})
                    else:
                        print("FINAL_SERIALIZERS", final_serializer.errors)
                        return JsonResponse({"data":final_serializer.errors})

                else:
                    print("DELIVERY SERIALIZER", delivery_serializer.errors)
                    return JsonResponse({"status": 400, "message": "Bad Request", "data": delivery_serializer.errors})
            else:
                print("APGAR SERIALIZER", apgar_serializer.errors)
                return JsonResponse({"status": 400, "message": "Bad Request", "data":apgar_serializer.errors})

        return JsonResponse({"status":400, "message":"Bad Request"})


class ReadDeliveryRecordView(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        id_received = json_object.get('id')
        data = {}
        if not id_received:
            return JsonResponse({"status":200, "message":"Bad Request"})
        if DeliveryRecord.objects.filter(id=id_received).exists():
            delivery_obj = DeliveryRecord.objects.get(id=id_received)
            delivery_data_serializer = DeliveryDataFESerializer(delivery_obj)
            data["delivery_data"] = delivery_data_serializer.data
            serializer = DeliveryRecordSerializer(delivery_obj)
            read_serializer = DeliveryRecordReadSerializer(data=serializer.data)
            if read_serializer.is_valid():
                final_read_serializer = DeliveryRecordReadFinalSerializer(data=read_serializer.data)
                print("READ SERIALIZER", read_serializer.data)
                if final_read_serializer.is_valid():
                    data["apgar_score"] = final_read_serializer.data
                    return JsonResponse({"status":200, "message":"Success", "data":data})
                else:
                    return JsonResponse({"data":final_read_serializer.errors})
            else:
                return JsonResponse({"data":read_serializer.errors})
        else:
            return JsonResponse({"status": 200, "message": "Bad Request"})



class CreateDeliveryRecordView(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        apgar_score = json_object.get("apgar_score")
        print("APGAR SCORE", apgar_score)
        delivery_data = json_object.get("delivery_data")
        live_birth = delivery_data.get("live_birth")
        still_birth = delivery_data.get("still_birth")
        age = int(delivery_data.get("age"))
        weight = float(delivery_data.get("weight"))
        data = {}
        if not delivery_data.get("preterm") == "":
            preterm = int(delivery_data.get("preterm", 0))
        else:
            preterm = 0
        delivery_data["preterm"] = preterm
        delivery_data["live_birth"] = live_birth
        delivery_data["still_birth"] = still_birth
        delivery_data["age"] = age
        delivery_data["weight"] = weight
        print("DELIVERY DATA", delivery_data)
        final_data = {}
        apgar_serializer = DeliveryRecordFrontEndSerializer(data=apgar_score)
        if apgar_serializer.is_valid():
            print(apgar_serializer.data)
            final_data.update(heart_rate_1_min_value=apgar_serializer.data["heart_rate_1_min_value"])
            final_data.update(heart_rate_1_min_slot=apgar_serializer.data["heart_rate_1_min_slot"])
            final_data.update(respiratory_effort_1_min_value=apgar_serializer.data["respiratory_effort_1_min_value"])
            final_data.update(respiratory_effort_1_min_slot=apgar_serializer.data["respiratory_effort_1_min_slot"])
            final_data.update(muscle_tone_1_min_value=apgar_serializer.data["muscle_tone_1_min_value"])
            final_data.update(muscle_tone_1_min_slot=apgar_serializer.data["muscle_tone_1_min_slot"])
            final_data.update(reflex_1_min_value=apgar_serializer.data["reflex_1_min_value"])
            final_data.update(reflex_1_min_slot=apgar_serializer.data["reflex_1_min_slot"])
            final_data.update(colour_1_min_value=apgar_serializer.data["colour_1_min_value"])
            final_data.update(colour_1_min_slot=apgar_serializer.data["colour_1_min_slot"])

            final_data.update(heart_rate_5_min_value=apgar_serializer.data["heart_rate_5_min_value"])
            final_data.update(heart_rate_5_min_slot=apgar_serializer.data["heart_rate_5_min_slot"])
            final_data.update(respiratory_effort_5_min_value=apgar_serializer.data["respiratory_effort_5_min_value"])
            final_data.update(respiratory_effort_5_min_slot=apgar_serializer.data["respiratory_effort_5_min_slot"])
            final_data.update(muscle_tone_5_min_value=apgar_serializer.data["muscle_tone_5_min_value"])
            final_data.update(muscle_tone_5_min_slot=apgar_serializer.data["muscle_tone_5_min_slot"])
            final_data.update(reflex_5_min_value=apgar_serializer.data["reflex_5_min_value"])
            final_data.update(reflex_5_min_slot=apgar_serializer.data["reflex_5_min_slot"])
            final_data.update(colour_5_min_value=apgar_serializer.data["colour_5_min_value"])
            final_data.update(colour_5_min_slot=apgar_serializer.data["colour_5_min_slot"])

            final_data.update(type_of_delivery=delivery_data.get("type_of_delivery"))
            final_data.update(sex=delivery_data.get("sex"))
            final_data.update(live_birth=delivery_data.get("live_birth"))
            final_data.update(still_birth=delivery_data.get("still_birth"))
            final_data.update(preterm=delivery_data.get("preterm"))
            final_data.update(abortion_types=delivery_data.get("abortion_types"))
            final_data.update(listing_id=delivery_data.get("listing_id"))
            final_data.update(name=delivery_data.get("name"))
            final_data.update(age=delivery_data.get("age"))
            final_data.update(weight=delivery_data.get("weight"))
        else:
            return JsonResponse({"status":400, "message":"Bad Request","apgar_": apgar_serializer.errors})
        # return JsonResponse({"data":final_data})
        # print(final_data)
        #
        final_serializer = DeliveryRecordSerializer(data=final_data)
        print(final_data)
        if final_serializer.is_valid():
            final_serializer.save()

            read_serializer = DeliveryRecordReadSerializer(data=final_serializer.data)
            if read_serializer.is_valid():
                final_read_serializer = DeliveryRecordReadFinalSerializer(data=read_serializer.data)
                if final_read_serializer.is_valid():
                    return JsonResponse({"status":200, "message":"success", "data":final_read_serializer.data})
            else:
                return JsonResponse({"status":400, "message":"Bad Requests", "data":read_serializer.errors})

        else:
            return JsonResponse({"status":400, "message":"Bad Request", "errors":final_serializer.errors})

        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse({serializer.data})
        # else:
        #     return JsonResponse({serializer.errors})errors

class DeliveryRecordsListing(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        listing_id = json_object.get("listing_id", None)
        if not listing_id:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"Listing ID is required"})
        if DeliveryRecord.objects.filter(listing_id=listing_id).exists():
            delivery_objects = DeliveryRecord.objects.filter(listing_id=int(listing_id)).order_by('-pk')
            serializer = DeliveryRecordListSerializer(delivery_objects, many=True)
            return JsonResponse({"status":200, "message":"success", "data":serializer.data})
        else:
            return JsonResponse({"status": 400, "message": "Bad Request", "data": "No such Hospital Exists"})

class DeleteDeliveryRecord(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        id = json_object.get("id", None)
        if not id:
            return JsonResponse({"status": 400, "message": "Bad Request", "data": "ID is required"})
        if DeliveryRecord.objects.filter(id=id).exists():
            obj = DeliveryRecord.objects.get(id=id)
            obj.delete()
            return JsonResponse({"status": 200, "message": "success", "data": "Entries Deleted"})
        else:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"Entry does not exist"})

