import json
from .models import ObstetricForm, ObstetricPhysicalExamination
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import ObstetricFormSerializer, PhysicalExaminationSerializer


class ObstetricFomCreateView(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        obstetric_form = json_object.get("obstetric_form", None)
        physical_examination = json_object.get("physical_examination", None)
        if not obstetric_form and not physical_examination:
            return JsonResponse({"status": 400, "message": "Bad Request"})
        obs_serializer = ObstetricFormSerializer(data=obstetric_form)
        if obs_serializer.is_valid():
            obs_serializer.save()
            print("obs_serializer", obs_serializer.data)
            pkk = obs_serializer.data['id']
            print("PKK", pkk)
            obs_response = obs_serializer.data
        else:
            return JsonResponse({"status": 400, "message": "Bad Request", "data":obs_serializer.errors})
        physical_examination["obstetric"] = pkk
        p_e_serializer = PhysicalExaminationSerializer(data=physical_examination)
        if p_e_serializer.is_valid():
            p_e_serializer.save()
            p_e_response = p_e_serializer.data
        else:
            return JsonResponse({"status": 400, "message": "Bad Request", "obstetric_data": obs_response,
                                 "physical_examination": p_e_serializer.errors})
        return JsonResponse(
            {"status": 200, "message": "Success", "obstetric_data": obs_response, "physical_examination": p_e_response})


class ObstetricFormUpdateView(generics.GenericAPIView):
    def post(self, request):
        json_body = json.loads(request.body)
        json_object = json_body.get("obstetric_form", None)
        obs_id = json_object.get("id", None)
        json_object2 = json_body.get("physical_examination", None)
        phy_id = json_object2.get("id", None)
        obs_data = {}
        phy_data = {}
        if json_object:
            obs_id = int(obs_id)
            if not obs_id:
                return JsonResponse({"status": 400, "message": "Bad Request", "data": "ID is required"})
        if json_object2:
            phy_id = int(phy_id)
            if not phy_id:
                return JsonResponse({"status": 400, "message": "Bad Request", "data": "ID is required"})

        if json_object:
            if ObstetricForm.objects.filter(id=obs_id).exists():
                obs_object = ObstetricForm.objects.get(id=obs_id)
                print("OBS OBJECT",obs_object)
                obs_object.hypertension = json_object.get("hypertension", obs_object.hypertension)
                obs_object.name = json_object.get("name", obs_object.name)
                obs_object.age = json_object.get("age", obs_object.age)
                obs_object.phone_no = json_object.get("phone_no", obs_object.phone_no)
                obs_object.history = json_object.get("history", obs_object.history)
                obs_object.hospital_id = json_object.get("hospital_id", obs_object.hospital_id)
                print("Hypertension",obs_object.hypertension)
                obs_object.diabetes = json_object.get("diabetes", obs_object.diabetes)
                obs_object.sexually_transmitted_disease = json_object.get("sexually_transmitted_disease",
                                                                          obs_object.sexually_transmitted_disease)
                obs_object.pyelonephritis_uti = json_object.get("pyelonephritis_uti", obs_object.pyelonephritis_uti)
                obs_object.acute_surgical_problem = json_object.get("acute_surgical_problem",
                                                                    obs_object.acute_surgical_problem)
                obs_object.genital_tract_abnormalities = json_object.get("genital_tract_abnormalities",
                                                                         obs_object.genital_tract_abnormalities)
                obs_object.maternal_age = json_object.get("maternal_age", obs_object.maternal_age)
                obs_object.maternal_weight = json_object.get("maternal_weight", obs_object.maternal_weight)
                obs_object.maternal_height = json_object.get("maternal_height", obs_object.maternal_height)
                obs_object.exposure_of_teratogens = json_object.get("exposure_of_teratogens",
                                                                    obs_object.exposure_of_teratogens)
                obs_object.exposure_to_mercury = json_object.get("exposure_to_mercury", obs_object.exposure_to_mercury)
                obs_object.prior_stillbirth = json_object.get("prior_stillbirth", obs_object.prior_stillbirth)
                obs_object.prior_preterm_delivery = json_object.get("prior_preterm_delivery",
                                                                    obs_object.prior_preterm_delivery)
                obs_object.prior_neonate_with_genitic_or_congenital_disorder = json_object.get(
                    "prior_neonate_with_genitic_or_congenital_disorder",
                    obs_object.prior_neonate_with_genitic_or_congenital_disorder)
                obs_object.polyhydramnios_and_oligohydramnios = json_object.get("polyhydramnios_and_oligohydramnios",
                                                                                obs_object.polyhydramnios_and_oligohydramnios)
                obs_object.multifetal_pregnancy = json_object.get("multifetal_pregnancy", obs_object.multifetal_pregnancy)
                obs_object.prior_birth_injury = json_object.get("prior_birth_injury", obs_object.prior_birth_injury)
                obs_object.gravidity_and_parity = json_object.get("gravidity_and_parity", obs_object.gravidity_and_parity)
                obs_object.created_by = json_object.get("created_by", obs_object.created_by)
                obs_object.modified_by = json_object.get("modified_by", obs_object.modified_by)
                obs_object.save()
                obs_serializer = ObstetricFormSerializer(obs_object)
                obs_data = obs_serializer.data
            else:
                obs_data = {}

        if json_object2:
            if ObstetricPhysicalExamination.objects.filter(id=phy_id).exists():
                p_e_object = ObstetricPhysicalExamination.objects.get(id=phy_id)
                p_e_object.lesions_or_discharge = json_object2.get("lesions_or_discharge",
                                                                  p_e_object.lesions_or_discharge)
                p_e_object.colour_and_consistency_of_cervix = json_object2.get("colour_and_consistency_of_cervix",
                                                                              p_e_object.colour_and_consistency_of_cervix)
                p_e_object.cervical_samples_for_testing = json_object2.get("cervical_samples_for_testing",
                                                                          p_e_object.cervical_samples_for_testing)
                p_e_object.pelvic_capacity = json_object2.get("pelvic_capacity", p_e_object.pelvic_capacity)
                p_e_object.blood_pressure = json_object2.get("blood_pressure", p_e_object.blood_pressure)
                p_e_object.weight = json_object2.get("weight", p_e_object.weight)
                p_e_object.uterine_size = json_object2.get("uterine_size", p_e_object.uterine_size)
                p_e_object.fundal_weight = json_object2.get("fundal_weight", p_e_object.fundal_weight)
                p_e_object.fetal_heart_rate_and_activity = json_object2.get("fetal_heart_rate_and_activity",
                                                                           p_e_object.fetal_heart_rate_and_activity)
                p_e_object.maternal_diet = json_object2.get("maternal_diet", p_e_object.maternal_diet)
                p_e_object.weight_gain = json_object2.get("weight_gain", p_e_object.weight_gain)
                p_e_object.date_of_examination = json_object2.get("date_of_examination", p_e_object.date_of_examination)
                p_e_object.visit_no = json_object2.get("visit_no", p_e_object.visit_no)
                p_e_object.created_by = json_object2.get("created_by", p_e_object.created_by)
                p_e_object.modified_by = json_object2.get("modified_by", p_e_object.modified_by)
                p_e_object.save()
                p_e_serializer = PhysicalExaminationSerializer(p_e_object)
                phy_data = p_e_serializer.data
            else:
                phy_data = {}
        return JsonResponse({"status":200, "message":"success", "data":{"obstetric_form":obs_data,
                                                                        "physical_examination":phy_data}})


class PhysicalExamUpdateView(generics.GenericAPIView):
    def post(self, request):
        json_body = json.loads(request.body)
        json_object = json_body.get("physical_examination")
        id = json_object.get("id", None)
        if not id:
            return JsonResponse({"status": 400, "message": "Bad Request", "data": "ID is required"})
        if ObstetricPhysicalExamination.objects.filter(id=id).exists():
            p_e_object = ObstetricPhysicalExamination.objects.get(id=id)
            p_e_object.lesions_or_discharge = json_object.get("lesions_or_discharge", p_e_object.lesions_or_discharge)
            p_e_object.colour_and_consistency_of_cervix = json_object.get("colour_and_consistency_of_cervix",
                                                                          p_e_object.colour_and_consistency_of_cervix)
            p_e_object.cervical_samples_for_testing = json_object.get("cervical_samples_for_testing",
                                                                      p_e_object.cervical_samples_for_testing)
            p_e_object.pelvic_capacity = json_object.get("pelvic_capacity", p_e_object.pelvic_capacity)
            p_e_object.blood_pressure = json_object.get("blood_pressure", p_e_object.blood_pressure)
            p_e_object.weight = json_object.get("weight", p_e_object.weight)
            p_e_object.uterine_size = json_object.get("uterine_size", p_e_object.uterine_size)
            p_e_object.fundal_weight = json_object.get("fundal_weight", p_e_object.fundal_weight)
            p_e_object.fetal_heart_rate_and_activity = json_object.get("fetal_heart_rate_and_activity",
                                                                       p_e_object.fetal_heart_rate_and_activity)
            p_e_object.maternal_diet = json_object.get("maternal_diet", p_e_object.maternal_diet)
            p_e_object.weight_gain = json_object.get("weight_gain", p_e_object.weight_gain)
            p_e_object.date_of_examination = json_object.get("date_of_examination", p_e_object.date_of_examination)
            p_e_object.visit_no = json_object.get("visit_no", p_e_object.visit_no)
            p_e_object.created_by = json_object.get("created_by", p_e_object.created_by)
            p_e_object.modified_by = json_object.get("modified_by", p_e_object.modified_by)
            p_e_object.save()
            p_e_serializer = PhysicalExaminationSerializer(p_e_object)
            return JsonResponse({"status": 200, "message": "success", "data": p_e_serializer.data})
        else:
            return JsonResponse({"status": 400, "message": "Bad Request", "data": "ID does not exist"})


class ObstetricListView(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        hospital_id = json_object.get("hospital_id", None)
        if not hospital_id:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"Hospital ID is required"})
        obs_records = ObstetricForm.objects.filter(hospital_id=hospital_id).order_by('-pk')
        serializer = ObstetricFormSerializer(obs_records, many=True)
        return JsonResponse({"status":200, "message":"Success", "data":serializer.data})


class ObstetricReadView(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        id = json_object.get("id", None)
        if not id:
            return JsonResponse({"status": 400, "message": "Bad Request", "data": "ID is required"})
        id = int(id)
        if ObstetricForm.objects.filter(id=id).exists():
            obs = ObstetricForm.objects.get(id=id)
            obs_serializer = ObstetricFormSerializer(obs)
            if ObstetricPhysicalExamination.objects.filter(obstetric=id).exists():
                physical_exams = ObstetricPhysicalExamination.objects.filter(obstetric=id)
                p_serializer = PhysicalExaminationSerializer(physical_exams, many=True)
                return JsonResponse({"status":200, "message":"Success", "data":{"obstetric_record":obs_serializer.data,
                                                                                "physical_examinations":p_serializer.data}})

            return JsonResponse({"status": 200, "message": "Success", "data": {"obstetric_record": obs_serializer.data,
                                                                               "physical_examinations": []}})
        else:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"Entry does not exist"})


class ObstetricDeleteView(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        id = json_object.get("id", None)
        if not id:
            return JsonResponse({"status": 400, "message": "Bad Request", "data": "ID is required"})
        id = int(id)
        if ObstetricForm.objects.filter(id=id).exists():
            obs = ObstetricForm.objects.get(id=id)
            if ObstetricPhysicalExamination.objects.filter(obstetric=id).exists():
                phy = ObstetricPhysicalExamination.objects.filter(obstetric=id)
                for ph in phy:
                    ph.delete()
            obs.delete()
            return JsonResponse({"status":200, "message":"success", "data":"Entries Deleted"})
        else:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"Entry does not exist"})

class DeletePhysicalExam(generics.GenericAPIView):
    def post(self, request):
        json_object = json.loads(request.body)
        id = json_object.get("id", None)
        if not id:
            return JsonResponse({"status": 400, "message": "Bad Request", "data": "ID is required"})
        id = int(id)
        if ObstetricPhysicalExamination.objects.filter(id=id).exists():
            phy = ObstetricPhysicalExamination.objects.get(id=id)
            phy.delete()
            return JsonResponse({"status": 200, "message": "success", "data": "Entries Deleted"})
        else:
            return JsonResponse({"status":400, "message":"Bad Request", "data":"Entry does not exist"})
