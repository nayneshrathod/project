from rest_framework import serializers


class DeliveryRecordReadSerializer(serializers.Serializer):
    id = serializers.CharField()
    heart_rate_1_0 = serializers.SerializerMethodField()
    heart_rate_1_1 = serializers.SerializerMethodField()
    heart_rate_1_2 = serializers.SerializerMethodField()
    heart_rate_1_min_value = serializers.CharField(allow_blank=True)
    heart_rate_1_min_slot = serializers.IntegerField(allow_null=True)
    resperatory_rate_1_0 = serializers.SerializerMethodField()
    resperatory_rate_1_1 = serializers.SerializerMethodField()
    resperatory_rate_1_2 = serializers.SerializerMethodField()
    respiratory_effort_1_min_value = serializers.CharField(allow_blank=True)
    respiratory_effort_1_min_slot = serializers.IntegerField(allow_null=True)
    muscle_tone_1_0 = serializers.SerializerMethodField()
    muscle_tone_1_1 = serializers.SerializerMethodField()
    muscle_tone_1_2 = serializers.SerializerMethodField()
    muscle_tone_1_min_value = serializers.CharField(allow_blank=True)
    muscle_tone_1_min_slot = serializers.IntegerField(allow_null=True)
    reflex_irritability_1_0 = serializers.SerializerMethodField()
    reflex_irritability_1_1 = serializers.SerializerMethodField()
    reflex_irritability_1_2 = serializers.SerializerMethodField()
    reflex_1_min_value = serializers.CharField(allow_blank=True)
    reflex_1_min_slot = serializers.IntegerField(allow_null=True)
    color_1_0 = serializers.SerializerMethodField()
    color_1_1 = serializers.SerializerMethodField()
    color_1_2 = serializers.SerializerMethodField()
    colour_1_min_value = serializers.CharField(allow_blank=True)
    colour_1_min_slot = serializers.IntegerField(allow_null=True)

    heart_rate_5_0 = serializers.SerializerMethodField()
    heart_rate_5_1 = serializers.SerializerMethodField()
    heart_rate_5_2 = serializers.SerializerMethodField()
    heart_rate_5_min_value = serializers.CharField(allow_blank=True)
    heart_rate_5_min_slot = serializers.IntegerField(allow_null=True)
    resperatory_rate_5_0 = serializers.SerializerMethodField()
    resperatory_rate_5_1 = serializers.SerializerMethodField()
    resperatory_rate_5_2 = serializers.SerializerMethodField()
    respiratory_effort_5_min_value = serializers.CharField(allow_blank=True)
    respiratory_effort_5_min_slot = serializers.IntegerField(allow_null=True)
    muscle_tone_5_0 = serializers.SerializerMethodField()
    muscle_tone_5_1 = serializers.SerializerMethodField()
    muscle_tone_5_2 = serializers.SerializerMethodField()
    muscle_tone_5_min_value = serializers.CharField(allow_blank=True)
    muscle_tone_5_min_slot = serializers.IntegerField(allow_null=True)
    reflex_irritability_5_0 = serializers.SerializerMethodField()
    reflex_irritability_5_1 = serializers.SerializerMethodField()
    reflex_irritability_5_2 = serializers.SerializerMethodField()
    reflex_5_min_value = serializers.CharField(allow_blank=True)
    reflex_5_min_slot = serializers.IntegerField(allow_null=True)
    color_5_0 = serializers.SerializerMethodField()
    color_5_1 = serializers.SerializerMethodField()
    color_5_2 = serializers.SerializerMethodField()
    colour_5_min_value = serializers.CharField(allow_blank=True)
    colour_5_min_slot = serializers.IntegerField(allow_null=True)

    def get_heart_rate_1_0(self, object):
        if object["heart_rate_1_min_slot"] == 0:
            return "{}".format(object["heart_rate_1_min_value"])
        else:
            return "-"

    def get_heart_rate_1_1(self, object):
        if object["heart_rate_1_min_slot"] == 1:
            return "{}".format(object["heart_rate_1_min_value"])
        else:
            return "-"

    def get_heart_rate_1_2(self, object):
        if object["heart_rate_1_min_slot"] == 2:
            return "{}".format(object["heart_rate_1_min_value"])
        else:
            return "-"

    def get_heart_rate_5_0(self, object):
        if object["heart_rate_5_min_slot"] == 0:
            return "{}".format(object["heart_rate_5_min_value"])
        else:
            return "-"
    def get_heart_rate_5_1(self, object):
        if object["heart_rate_5_min_slot"] == 1:
            return "{}".format(object["heart_rate_5_min_value"])
        else:
            return "-"
    def get_heart_rate_5_2(self, object):
        if object["heart_rate_5_min_slot"] == 2:
            return "{}".format(object["heart_rate_5_min_value"])
        else:
            return "-"
    def get_resperatory_rate_1_0(self, object):
        if object["respiratory_effort_1_min_slot"] == 0:
            return "{}".format(object["respiratory_effort_1_min_value"])
        else:
            return "-"

    def get_resperatory_rate_1_1(self, object):
        if object["respiratory_effort_1_min_slot"] == 1:
            return "{}".format(object["respiratory_effort_1_min_value"])
        else:
            return "-"

    def get_resperatory_rate_1_2(self, object):
        if object["respiratory_effort_1_min_slot"] == 2:
            return "{}".format(object["respiratory_effort_1_min_value"])
        else:
            return "-"

    def get_resperatory_rate_5_0(self, object):
        if object["respiratory_effort_5_min_slot"] == 0:
            return "{}".format(object["respiratory_effort_5_min_value"])
        else:
            return "-"

    def get_resperatory_rate_5_1(self, object):
        if object["respiratory_effort_5_min_slot"] == 1:
            return "{}".format(object["respiratory_effort_5_min_value"])
        else:
            return "-"

    def get_resperatory_rate_5_2(self, object):
        if object["respiratory_effort_5_min_slot"] == 0:
            return "{}".format(object["respiratory_effort_5_min_value"])
        else:
            return "-"

    def get_muscle_tone_1_0(self, object):
        if object["muscle_tone_1_min_slot"] == 0:
            return "{}".format(object["muscle_tone_1_min_value"])
        else:
            return "-"

    def get_muscle_tone_1_1(self, object):
        if object["muscle_tone_1_min_slot"] == 1:
            return "{}".format(object["muscle_tone_1_min_value"])
        else:
            return "-"

    def get_muscle_tone_1_2(self, object):
        if object["muscle_tone_1_min_slot"] == 2:
            return "{}".format(object["muscle_tone_1_min_value"])
        else:
            return "-"

    def get_muscle_tone_5_0(self, object):
        if object["muscle_tone_5_min_slot"] == 0:
            return "{}".format(object["muscle_tone_5_min_value"])
        else:
            return "-"

    def get_muscle_tone_5_1(self, object):
        if object["muscle_tone_5_min_slot"] == 1:
            return "{}".format(object["muscle_tone_5_min_value"])
        else:
            return "-"

    def get_muscle_tone_5_2(self, object):
        if object["muscle_tone_5_min_slot"] == 0:
            return "{}".format(object["muscle_tone_5_min_value"])
        else:
            return "-"

    def get_reflex_irritability_1_0(self, object):
        if object["reflex_1_min_slot"] == 0:
            return "{}".format(object["reflex_1_min_value"])
        else:
            return "-"

    def get_reflex_irritability_1_1(self, object):
        if object["reflex_1_min_slot"] == 1:
            return "{}".format(object["reflex_1_min_value"])
        else:
            return "-"

    def get_reflex_irritability_1_2(self, object):
        if object["reflex_1_min_slot"] == 2:
            return "{}".format(object["reflex_1_min_value"])
        else:
            return "-"

    def get_reflex_irritability_5_0(self, object):
        if object["reflex_5_min_slot"] == 0:
            return "{}".format(object["reflex_5_min_value"])
        else:
            return "-"

    def get_reflex_irritability_5_1(self, object):
        if object["reflex_5_min_slot"] == 1:
            return "{}".format(object["reflex_5_min_value"])
        else:
            return "-"

    def get_reflex_irritability_5_2(self, object):
        if object["reflex_5_min_slot"] == 2:
            return "{}".format(object["reflex_5_min_value"])
        else:
            return "-"

    def get_color_1_0(self, object):
        if object["colour_1_min_slot"] == 0:
            return "{}".format(object["colour_1_min_value"])
        else:
            return "-"

    def get_color_1_1(self, object):
        if object["colour_1_min_slot"] == 1:
            return "{}".format(object["colour_1_min_value"])
        else:
            return "-"

    def get_color_1_2(self, object):
        if object["colour_1_min_slot"] == 2:
            return "{}".format(object["colour_1_min_value"])
        else:
            return "-"

    def get_color_5_0(self, object):
        if object["colour_5_min_slot"] == 0:
            return "{}".format(object["colour_5_min_value"])
        else:
            return "-"

    def get_color_5_1(self, object):
        if object["colour_5_min_slot"] == 1:
            return "{}".format(object["colour_5_min_value"])
        else:
            return "-"

    def get_color_5_2(self, object):
        if object["colour_5_min_slot"] == 2:
            return "{}".format(object["colour_5_min_value"])
        else:
            return "-"




class DeliveryRecordReadFinalSerializer(serializers.Serializer):
    id = serializers.CharField()
    heart_rate_1_0 = serializers.CharField(allow_blank=True)
    heart_rate_1_1 = serializers.CharField(allow_blank=True)
    heart_rate_1_2 = serializers.CharField(allow_blank=True)
    resperatory_rate_1_0 = serializers.CharField(allow_blank=True)
    resperatory_rate_1_1 = serializers.CharField(allow_blank=True)
    resperatory_rate_1_2 = serializers.CharField(allow_blank=True)
    muscle_tone_1_0 = serializers.CharField(allow_blank=True)
    muscle_tone_1_1 = serializers.CharField(allow_blank=True)
    muscle_tone_1_2 = serializers.CharField(allow_blank=True)
    reflex_irritability_1_0 = serializers.CharField(allow_blank=True)
    reflex_irritability_1_1 = serializers.CharField(allow_blank=True)
    reflex_irritability_1_2 = serializers.CharField(allow_blank=True)
    color_1_0 = serializers.CharField(allow_blank=True)
    color_1_1 = serializers.CharField(allow_blank=True)
    color_1_2 = serializers.CharField(allow_blank=True)

    heart_rate_5_0 = serializers.CharField(allow_blank=True)
    heart_rate_5_1 = serializers.CharField(allow_blank=True)
    heart_rate_5_2 = serializers.CharField(allow_blank=True)
    resperatory_rate_5_0 = serializers.CharField(allow_blank=True)
    resperatory_rate_5_1 = serializers.CharField(allow_blank=True)
    resperatory_rate_5_2 = serializers.CharField(allow_blank=True)
    muscle_tone_5_0 = serializers.CharField(allow_blank=True)
    muscle_tone_5_1 = serializers.CharField(allow_blank=True)
    muscle_tone_5_2 = serializers.CharField(allow_blank=True)
    reflex_irritability_5_0 = serializers.CharField(allow_blank=True)
    reflex_irritability_5_1 = serializers.CharField(allow_blank=True)
    reflex_irritability_5_2 = serializers.CharField(allow_blank=True)
    color_5_0 = serializers.CharField(allow_blank=True)
    color_5_1 = serializers.CharField(allow_blank=True)
    color_5_2 = serializers.CharField(allow_blank=True)


'''

final_data['id'] = delivery_data.get('id')
            final_data['type_of_delivery'] = delivery_data.get('type_of_delivery')
            final_data['sex'] = delivery_data.get('sex')
            final_data['live_birth'] = delivery_data.get('live_birth')
            final_data['still_birth'] = delivery_data.get('still_birth')
            final_data['preterm'] = delivery_data.get('preterm')
            final_data['abortion_types'] = delivery_data.get('abortion_types')

            heart_rate_1 = delivery_data.get('heart_rate_1_min_slot')
            muscle_tone_1 = delivery_data.get('muscle_tone_1_min_slot')
            reflex_1 = delivery_data.get('reflex_1_min_slot')
            colour_1 = delivery_data.get('colour_1_min_slot')
            respiratory_1 = delivery_data.get('respiratory_effort_1_min_slot')

            heart_rate_5 = delivery_data.get('heart_rate_5_min_slot')
            muscle_tone_5 = delivery_data.get('muscle_tone_5_min_slot')
            reflex_5 = delivery_data.get('reflex_5_min_slot')
            colour_5 = delivery_data.get('colour_5_min_slot')
            respiratory_5 = delivery_data.get('respiratory_effort_5_min_slot')

            print(heart_rate_1)
            print(muscle_tone_1)
            print(reflex_1)
            print(colour_1)
            print(respiratory_1)

            if heart_rate_1 == 0:
                final_data['heart_rate_1_0'] = delivery_data.get('heart_rate_1_min_value')
                final_data['heart_rate_1_1'] = ""
                final_data['heart_rate_1_2'] = ""

            elif heart_rate_1 == 1:
                final_data['heart_rate_1_0'] = ""
                final_data['heart_rate_1_1'] = delivery_data.get('heart_rate_1_min_value')
                final_data['heart_rate_1_2'] = ""

            else:
                final_data['heart_rate_1_0'] = ""
                final_data['heart_rate_1_1'] = ""
                final_data['heart_rate_1_2'] = delivery_data.get('heart_rate_1_min_value')

            if muscle_tone_1 == 0:
                final_data['muscle_tone_1_0'] = delivery_data.get('muscle_tone_1_min_value')
                final_data['muscle_tone_1_1'] = ""
                final_data['muscle_tone_1_2'] = ""

            elif muscle_tone_1 == 1:
                final_data['muscle_tone_1_0'] = ""
                final_data['muscle_tone_1_1'] = delivery_data.get('muscle_tone_1_min_value')
                final_data['muscle_tone_1_2'] = ""

            else:
                final_data['muscle_tone_1_0'] = ""
                final_data['muscle_tone_1_1'] = ""
                final_data['muscle_tone_1_2'] = delivery_data.get('muscle_tone_1_min_value')

            if reflex_1 == 0:
                final_data['reflex_irritability_1_0'] = delivery_data.get('reflex_1_min_value')
                final_data['reflex_irritability_1_1'] = ""
                final_data['reflex_irritability_1_2'] = ""

            elif reflex_1 == 1:
                final_data['reflex_irritability_1_0'] = ""
                final_data['reflex_irritability_1_1'] = delivery_data.get('reflex_1_min_value')
                final_data['reflex_irritability_1_2'] = ""

            else:
                final_data['reflex_irritability_1_0'] = ""
                final_data['reflex_irritability_1_1'] = ""
                final_data['reflex_irritability_1_2'] = delivery_data.get('reflex_1_min_value')

            if colour_1 == 0:
                final_data['color_1_0'] = delivery_data.get('colour_1_min_value')
                final_data['color_1_1'] = ""
                final_data['color_1_2'] = ""

            elif colour_1 == 1:
                final_data['color_1_0'] = ""
                final_data['color_1_1'] = delivery_data.get('colour_1_min_value')
                final_data['color_1_2'] = ""

            else:
                final_data['color_1_0'] = ""
                final_data['color_1_1'] = ""
                final_data['color_1_2'] = delivery_data.get('colour_1_min_value')

            if respiratory_1 == 0:
                final_data['resperatory_rate_1_0'] = delivery_data.get('respiratory_effort_1_min_value')
                final_data['resperatory_rate_1_1'] = ""
                final_data['resperatory_rate_1_2'] = ""

            elif respiratory_1 == 1:
                final_data['resperatory_rate_1_0'] = ""
                final_data['resperatory_rate_1_1'] = delivery_data.get('respiratory_effort_1_min_value')
                final_data['resperatory_rate_1_2'] = ""

            else:
                final_data['resperatory_rate_1_0'] = ""
                final_data['resperatory_rate_1_1'] = ""
                final_data['resperatory_rate_1_2'] = delivery_data.get('respiratory_effort_1_min_value')

            if heart_rate_5 == 0:
                final_data['heart_rate_5_0'] = delivery_data.get('heart_rate_5_min_value')
                final_data['heart_rate_5_1'] = ""
                final_data['heart_rate_5_2'] = ""

            elif heart_rate_5 == 1:
                final_data['heart_rate_5_0'] = ""
                final_data['heart_rate_5_1'] = delivery_data.get('heart_rate_5_min_value')
                final_data['heart_rate_5_2'] = ""

            else:
                final_data['heart_rate_5_0'] = ""
                final_data['heart_rate_1_1'] = ""
                final_data['heart_rate_1_2'] = delivery_data.get('heart_rate_5_min_value')

            if muscle_tone_5 == 0:
                final_data['muscle_tone_5_0'] = delivery_data.get('muscle_tone_5_min_value')
                final_data['muscle_tone_5_1'] = ""
                final_data['muscle_tone_5_2'] = ""

            elif muscle_tone_5 == 1:
                final_data['muscle_tone_5_0'] = ""
                final_data['muscle_tone_5_1'] = delivery_data.get('muscle_tone_5_min_value')
                final_data['muscle_tone_5_2'] = ""

            else:
                final_data['muscle_tone_5_0'] = ""
                final_data['muscle_tone_5_1'] = ""
                final_data['muscle_tone_5_2'] = delivery_data.get('muscle_tone_5_min_value')

            if reflex_5 == 0:
                final_data['reflex_irritability_5_0'] = delivery_data.get('reflex_5_min_value')
                final_data['reflex_irritability_5_1'] = ""
                final_data['reflex_irritability_5_2'] = ""

            elif reflex_5 == 1:
                final_data['reflex_irritability_5_0'] = ""
                final_data['reflex_irritability_5_1'] = delivery_data.get('reflex_5_min_value')
                final_data['reflex_irritability_5_2'] = ""

            else:
                final_data['reflex_irritability_5_0'] = ""
                final_data['reflex_irritability_5_1'] = ""
                final_data['reflex_irritability_5_2'] = delivery_data.get('reflex_5_min_value')

            if colour_5 == 0:
                final_data['color_5_0'] = delivery_data.get('colour_5_min_value')
                final_data['color_5_1'] = ""
                final_data['color_5_2'] = ""

            elif colour_5 == 1:
                final_data['color_5_0'] = ""
                final_data['color_5_1'] = delivery_data.get('colour_5_min_value')
                final_data['color_5_2'] = ""

            else:
                final_data['color_5_0'] = ""
                final_data['color_5_1'] = ""
                final_data['color_5_2'] = delivery_data.get('colour_5_min_value')

            if respiratory_5 == 0:
                final_data['resperatory_rate_5_0'] = delivery_data.get('respiratory_effort_5_min_value')
                final_data['resperatory_rate_5_1'] = ""
                final_data['resperatory_rate_5_2'] = ""

            elif respiratory_5 == 1:
                final_data['resperatory_rate_5_0'] = ""
                final_data['resperatory_rate_5_1'] = delivery_data.get('respiratory_effort_5_min_value')
                final_data['resperatory_rate_5_2'] = ""

            else:
                final_data['resperatory_rate_5_0'] = ""
                final_data['resperatory_rate_5_1'] = ""
                final_data['resperatory_rate_5_2'] = delivery_data.get('respiratory_effort_5_min_value')

            print(final_data)
        return JsonResponse({"status":200,"message":"success","data": final_data})

'''