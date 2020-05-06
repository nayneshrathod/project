from .models import *
from rest_framework import serializers


class DeliveryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRecord
        fields = '__all__'

class DeliveryDataFESerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRecord
        fields = ("id", "name", "age", "weight", "type_of_delivery", "sex", "live_birth", "still_birth", "preterm", "listing_id")


class MTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTerminationOfPregnancyRecord
        fields = '__all__'

    def to_internal_value(self, data):
        mtp_rec = data['mtp_record']
        return super().to_internal_value(mtp_rec)


class MTPReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTerminationOfPregnancyRecord
        fields = '__all__'

    def to_representation(self, instance):
        char_fields = ['date_of_admission', 'name_of_patient', 'contact_name', 'reason_of_termination','phone',
                       'type_of_abortion', 'date_of_termination', 'date_of_discharge', 'results_and_remarks',
                       'post_abortion_complication_identified', 'post_abortion_complication_treated', 'created_at',
                       'modified_at']
        int_fields = ['age', 'weight','duration_of_pregnancy','created_by','modified_by','hospital_id']

        data = super(MTPReadSerializer, self).to_representation(instance)
        for field in char_fields:
            try:
                if not data[field]:
                    data[field] = ""
            except KeyError:
                pass
        for field in int_fields:
            try:
                if not data[field]:
                    data[field] = 0
            except KeyError:
                pass
        #        for field in decimal_fields:
        #            try:
        #                if not data[field]:
        #                    data[field] = 0.0
        #            except KeyError:
        #                pass
        # for field in bool_fields:
        #     try:
        #         if not data[field]:
        #             data[field] = False
        #     except KeyError:
        #         pass
        return data







class MTPListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTerminationOfPregnancyRecord
        fields = ['pk','name_of_patient', 'phone', 'date_of_admission', 'duration_of_pregnancy', 'type_of_abortion']

    # def to_representation(self, instance):
    #     # representation = super().to_representation(instance)
    #     mtp_list = dict()
    #     mtp


class MTPNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTerminationOfPregnancyRecord
        fields = '__all__'

    # def to_internal_value(self, data):
    #     mtp_rec = data['mtp_record']
    #     return super().to_internal_value(mtp_rec)


class DeliveryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRecord
        fields = '__all__'
    # # heart_rate_1_0 = serializers.CharField(max_length=10, allow_blank=True)
    # # heart_rate_1_1 = serializers.CharField(max_length=10, allow_blank=True)
    # # heart_rate_1_2 = serializers.CharField(max_length=10, allow_blank=True)
    #
    # # heart_rate_1_min_value = serializers.SerializerMethodField('get_heart_rate_1_min_value')
    # # heart_rate_1_min_slot = serializers.SerializerMethodField('get_heart_rate_1_min_slot')
    #
    #
    # def get_heart_rate_1_min_value(self, obj):
    #     print(obj)
    #     # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
    #     # for fld in fields_in_obj:
    #     #     if obj.fld:
    #     #        # return "{}".format(obj.fld)
    #     # return fields_in_obj
    #     if obj.heart_rate_1_0:
    #         return "{}".format(obj.heart_rate_1_0)
    #     elif obj.heart_rate_1_1:
    #         return "{}".format(obj.heart_rate_1_1)
    #     elif obj.heart_rate_1_2:
    #         return "{}".format(obj.heart_rate_1_2)
    #
    # def get_heart_rate_1_min_slot(self, obj):
    #     print(obj)
    #     # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
    #     if obj.heart_rate_1_0:
    #         return int(0)
    #     elif obj.heart_rate_1_1:
    #         return int(1)
    #     elif obj.heart_rate_1_2:
    #         return int(2)
    #
    # def create(self, validated_data):
    #     fields = ['heart_rate_1_min_value', 'heart_rate_1_min_slot', 'muscle_tone_1_min_value', 'muscle_tone_1_min_slot',
    #               'reflex_1_min_value', 'reflex_1_min_slot', 'colour_1_min_value', 'colour_1_min_slot', 'respiratory_effort_1_min_value',
    #               'respiratory_effort_1_min_slot']
    #
    #
    # class Meta:
    #     model = DeliveryRecord
    #     fields = ['heart_rate_1_0','heart_rate_1_1','heart_rate_1_2','heart_rate_1_min_value', 'heart_rate_1_min_slot', 'muscle_tone_1_min_value', 'muscle_tone_1_min_slot',
    #               'reflex_1_min_value', 'reflex_1_min_slot', 'colour_1_min_value', 'colour_1_min_slot', 'respiratory_effort_1_min_value',
    #               'respiratory_effort_1_min_slot']
    #
    #     # extra_kwargs = {
    #     #     'heart_rate_1_0': {'read_only': True},
    #     #     'heart_rate_1_1': {'read_only': True},
    #     #     'heart_rate_1_2': {'read_only': True},
    #     # }


class DeliveryRecordFrontEndSerializer(serializers.Serializer):
    heart_rate_1_0 = serializers.CharField(allow_blank=True, max_length=10)
    heart_rate_1_1 = serializers.CharField(allow_blank=True, max_length=10)
    heart_rate_1_2 = serializers.CharField(allow_blank=True, max_length=10)
    heart_rate_1_min_value = serializers.SerializerMethodField()
    heart_rate_1_min_slot = serializers.SerializerMethodField()
    resperatory_rate_1_0 = serializers.CharField(allow_blank=True, max_length=100)
    resperatory_rate_1_1 = serializers.CharField(allow_blank=True, max_length=100)
    resperatory_rate_1_2 = serializers.CharField(allow_blank=True, max_length=100)
    respiratory_effort_1_min_value = serializers.SerializerMethodField()
    respiratory_effort_1_min_slot = serializers.SerializerMethodField()
    muscle_tone_1_0 = serializers.CharField(allow_blank=True, max_length=100)
    muscle_tone_1_1 = serializers.CharField(allow_blank=True, max_length=100)
    muscle_tone_1_2 = serializers.CharField(allow_blank=True, max_length=100)
    muscle_tone_1_min_value = serializers.SerializerMethodField()
    muscle_tone_1_min_slot = serializers.SerializerMethodField()
    reflex_irritability_1_0 = serializers.CharField(allow_blank=True, max_length=100)
    reflex_irritability_1_1 = serializers.CharField(allow_blank=True, max_length=100)
    reflex_irritability_1_2 = serializers.CharField(allow_blank=True, max_length=100)
    reflex_1_min_value = serializers.SerializerMethodField()
    reflex_1_min_slot = serializers.SerializerMethodField()
    color_1_0 = serializers.CharField(allow_blank=True, max_length=100)
    color_1_1 = serializers.CharField(allow_blank=True, max_length=100)
    color_1_2 = serializers.CharField(allow_blank=True, max_length=100)
    colour_1_min_value = serializers.SerializerMethodField()
    colour_1_min_slot = serializers.SerializerMethodField()

    heart_rate_5_0 = serializers.CharField(allow_blank=True, max_length=10)
    heart_rate_5_1 = serializers.CharField(allow_blank=True, max_length=10)
    heart_rate_5_2 = serializers.CharField(allow_blank=True, max_length=10)
    heart_rate_5_min_value = serializers.SerializerMethodField()
    heart_rate_5_min_slot = serializers.SerializerMethodField()
    resperatory_rate_5_0 = serializers.CharField(allow_blank=True, max_length=100)
    resperatory_rate_5_1 = serializers.CharField(allow_blank=True, max_length=100)
    resperatory_rate_5_2 = serializers.CharField(allow_blank=True, max_length=100)
    respiratory_effort_5_min_value = serializers.SerializerMethodField()
    respiratory_effort_5_min_slot = serializers.SerializerMethodField()
    muscle_tone_5_0 = serializers.CharField(allow_blank=True, max_length=100)
    muscle_tone_5_1 = serializers.CharField(allow_blank=True, max_length=100)
    muscle_tone_5_2 = serializers.CharField(allow_blank=True, max_length=100)
    muscle_tone_5_min_value = serializers.SerializerMethodField()
    muscle_tone_5_min_slot = serializers.SerializerMethodField()
    reflex_irritability_5_0 = serializers.CharField(allow_blank=True, max_length=100)
    reflex_irritability_5_1 = serializers.CharField(allow_blank=True, max_length=100)
    reflex_irritability_5_2 = serializers.CharField(allow_blank=True, max_length=100)
    reflex_5_min_value = serializers.SerializerMethodField()
    reflex_5_min_slot = serializers.SerializerMethodField()
    color_5_0 = serializers.CharField(allow_blank=True, max_length=100)
    color_5_1 = serializers.CharField(allow_blank=True, max_length=100)
    color_5_2 = serializers.CharField(allow_blank=True, max_length=100)
    colour_5_min_value = serializers.SerializerMethodField()
    colour_5_min_slot = serializers.SerializerMethodField()

    # class Meta:
    #     fields = ["heart_rate_1_min_value", "heart_rate_1_min_slot"]

    def get_heart_rate_1_min_value(self, object):
        # json_obj = json.loads(object)
        if object['heart_rate_1_0']:
            return "{}".format(object["heart_rate_1_0"])
        elif object['heart_rate_1_1']:
            return "{}".format(object['heart_rate_1_1'])
        elif object['heart_rate_1_2']:
            return "{}".format(object["heart_rate_1_2"])
        else:
            return ""

    def get_heart_rate_1_min_slot(self, obj):
        # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
        if obj["heart_rate_1_0"]:
            return int(0)
        elif obj["heart_rate_1_1"]:
            return int(1)
        elif obj["heart_rate_1_2"]:
            return int(2)
        else:
            return None

    def get_respiratory_effort_1_min_value(self, object):
        # json_obj = json.loads(object)
        if object['resperatory_rate_1_0']:
            return "{}".format(object["resperatory_rate_1_0"])
        elif object['resperatory_rate_1_1']:
            return "{}".format(object['resperatory_rate_1_1'])
        elif object['resperatory_rate_1_2']:
            return "{}".format(object["resperatory_rate_1_2"])
        else:
            return ""

    def get_respiratory_effort_1_min_slot(self, obj):
        # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
        if obj["resperatory_rate_1_0"]:
            return int(0)
        elif obj["resperatory_rate_1_1"]:
            return int(1)
        elif obj["resperatory_rate_1_2"]:
            return int(2)
        else:
            return None

    def get_muscle_tone_1_min_value(self, object):
        # json_obj = json.loads(object)
        if object['muscle_tone_1_0']:
            return "{}".format(object["muscle_tone_1_0"])
        elif object['muscle_tone_1_1']:
            return "{}".format(object['muscle_tone_1_1'])
        elif object['muscle_tone_1_2']:
            return "{}".format(object["muscle_tone_1_2"])
        else:
            return ""

    def get_muscle_tone_1_min_slot(self, obj):
        # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
        if obj["muscle_tone_1_0"]:
            return int(0)
        elif obj["muscle_tone_1_1"]:
            return int(1)
        elif obj["muscle_tone_1_2"]:
            return int(2)
        else:
            return None

    def get_reflex_1_min_value(self, object):
        # json_obj = json.loads(object)
        if object['reflex_irritability_1_0']:
            return "{}".format(object["reflex_irritability_1_0"])
        elif object['reflex_irritability_1_1']:
            return "{}".format(object['reflex_irritability_1_1'])
        elif object['resperatory_rate_1_2']:
            return "{}".format(object["reflex_irritability_1_2"])
        else:
            return ""

    def get_reflex_1_min_slot(self, obj):
        # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
        if obj["reflex_irritability_1_0"]:
            return int(0)
        elif obj["reflex_irritability_1_1"]:
            return int(1)
        elif obj["reflex_irritability_1_2"]:
            return int(2)
        else:
            return None

    def get_colour_1_min_value(self, object):
        # json_obj = json.loads(object)
        if object['color_1_0']:
            return "{}".format(object["color_1_0"])
        elif object['color_1_1']:
            return "{}".format(object['color_1_1'])
        elif object['color_1_2']:
            return "{}".format(object["color_1_2"])
        else:
            return ""

    def get_colour_1_min_slot(self, obj):
        # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
        if obj["color_1_0"]:
            return int(0)
        elif obj["color_1_1"]:
            return int(1)
        elif obj["color_1_2"]:
            return int(2)
        else:
            return None

    def get_heart_rate_5_min_value(self, object):
        # json_obj = json.loads(object)
        if object['heart_rate_5_0']:
            return "{}".format(object["heart_rate_5_0"])
        elif object['heart_rate_5_1']:
            return "{}".format(object['heart_rate_5_1'])
        elif object['heart_rate_5_2']:
            return "{}".format(object["heart_rate_5_2"])
        else:
            return ""

    def get_heart_rate_5_min_slot(self, obj):
        # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
        if obj["heart_rate_5_0"]:
            return int(0)
        elif obj["heart_rate_5_1"]:
            return int(1)
        elif obj["heart_rate_5_2"]:
            return int(2)
        else:
            return None

    def get_respiratory_effort_5_min_value(self, object):
        # json_obj = json.loads(object)
        if object['resperatory_rate_5_0']:
            return "{}".format(object["resperatory_rate_5_0"])
        elif object['resperatory_rate_5_1']:
            return "{}".format(object['resperatory_rate_5_1'])
        elif object['resperatory_rate_5_2']:
            return "{}".format(object["resperatory_rate_5_2"])
        else:
            return ""

    def get_respiratory_effort_5_min_slot(self, obj):
        # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
        if obj["resperatory_rate_5_0"]:
            return int(0)
        elif obj["resperatory_rate_5_1"]:
            return int(1)
        elif obj["resperatory_rate_5_2"]:
            return int(2)
        else:
            return None

    def get_muscle_tone_5_min_value(self, object):
        # json_obj = json.loads(object)
        if object['muscle_tone_5_0']:
            return "{}".format(object["muscle_tone_5_0"])
        elif object['muscle_tone_5_1']:
            return "{}".format(object['muscle_tone_5_1'])
        elif object['muscle_tone_5_2']:
            return "{}".format(object["muscle_tone_5_2"])
        else:
            return ""

    def get_muscle_tone_5_min_slot(self, obj):
        # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
        if obj["muscle_tone_5_0"]:
            return int(0)
        elif obj["muscle_tone_5_1"]:
            return int(1)
        elif obj["muscle_tone_5_2"]:
            return int(2)
        else:
            return None

    def get_reflex_5_min_value(self, object):
        # json_obj = json.loads(object)
        if object['reflex_irritability_5_0']:
            return "{}".format(object["reflex_irritability_5_0"])
        elif object['reflex_irritability_5_1']:
            return "{}".format(object['reflex_irritability_5_1'])
        elif object['resperatory_rate_5_2']:
            return "{}".format(object["reflex_irritability_5_2"])
        else:
            return ""

    def get_reflex_5_min_slot(self, obj):
        # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
        if obj["reflex_irritability_5_0"]:
            return int(0)
        elif obj["reflex_irritability_5_1"]:
            return int(1)
        elif obj["reflex_irritability_5_2"]:
            return int(2)
        else:
            return None

    def get_colour_5_min_value(self, object):
        # json_obj = json.loads(object)
        if object['color_5_0']:
            return "{}".format(object["color_5_0"])
        elif object['color_5_1']:
            return "{}".format(object['color_5_1'])
        elif object['color_5_2']:
            return "{}".format(object["color_5_2"])
        else:
            return ""

    def get_colour_5_min_slot(self, obj):
        # fields_in_obj = ["heart_rate_1_0", "heart_rate_1_1", "heart_rate_1_2"]
        if obj["color_5_0"]:
            return int(0)
        elif obj["color_5_1"]:
            return int(1)
        elif obj["color_5_2"]:
            return int(2)
        else:
            return None

class DeliveryRecordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRecord
        fields = ("id", "listing_id", "name", "age", "type_of_delivery", "type_of_delivery")