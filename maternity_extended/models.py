from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from maternity.models import *


class MedicalTerminationOfPregnancyRecord(models.Model):
    ABORTION_CHOICES = (("Medical", 'Medical'),
                        ("Vaccum Aspiration - Surgical", 'Vaccum Aspiration - Surgical'),
                        ("Dilation & Curettage(D&C) - Surgical", 'Dilation & Curettage(D&C) - Surgical'),
                        ("Gravid Hysterectomy - Surgical", 'Gravid Hysterectomy - Surgical'),
                        ("Labour Induction Abortion", 'Labour Induction Abortion'))
    #
    date_of_admission = models.DateField(default="2019-12-13")
    hospital_id = models.IntegerField(null=True, blank=True)
    phone = models.CharField(blank=True, null=True, max_length=15)
    name_of_patient = models.CharField(max_length=100, default="name")
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(99)], blank=True, null=True)
    weight = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(999)], blank=True, null=True)
    duration_of_pregnancy = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(52)], blank=True,
                                                null=True)
    reason_of_termination = models.TextField(blank=True, null=True)
    type_of_abortion = models.CharField(max_length=100, choices=ABORTION_CHOICES, blank=True, null=True)
    date_of_termination = models.DateField(blank=True, null=True)
    date_of_discharge = models.DateField(blank=True, null=True)
    results_and_remarks = models.TextField(blank=True, null=True)
    treatment_given = models.TextField(blank=True, null=True)
    post_abortion_complication_identified = models.TextField(blank=True, null=True)
    post_abortion_complication_treated = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_at = models.DateField(auto_now_add=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "maternity_extended_medicalterminationofpregnancyrecord"
        app_label = "prescription"


#        db_table = medical_termination_of_pregnancy_record


class DeliveryRecord(models.Model):
    DELIVERY_TYPES = (
        ("Normal", "Normal"),
        ("Cesarean Birth (C-Section / LSCS)", "Cesarean Birth (C-Section / LSCS)"),
        ("Vaginal Birth After Cesarean (VBAC)","Vaginal Birth After Cesarean (VBAC)"),
        ("Instrumental Delivery","Instrumental Delivery"),
                      )
    GENDER = (("Male", "Male"),
              ("Female", "Female"),
              ("Other", "Other"))

    ABORTION_CHOICES = (("Medical", 'Medical'),
                        ("Vaccum Aspiration - Surgical", "Vaccum Aspiration - Surgical"),
                        ("Dilation & Curettage(D&C) - Surgical", "Dilation & Curettage(D&C) - Surgical"),
                        ("Gravid Hysterectomy - Surgical", "Gravid Hysterectomy - Surgical"),
                        ("Labour Induction Abortion", "Labour Induction Abortion"))

    patient_id = models.IntegerField(blank=True, null=True)
    listing_id = models.IntegerField()
    name = models.CharField(blank=True, null=True, max_length=100)
    age = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    maternity = models.ForeignKey(MaternityDetails, on_delete=models.CASCADE, blank=True, null=True)
    type_of_delivery = models.CharField(max_length=66, choices=DELIVERY_TYPES, blank=True, null=True)
    sex = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    live_birth = models.CharField(max_length=500,blank=True, null=True)
    still_birth = models.CharField(max_length=500, blank=True, null=True)
    preterm = models.IntegerField(MaxValueValidator(8), blank=True, null=True)
    abortion_types = models.CharField(max_length=50, choices=ABORTION_CHOICES, blank=True, null=True)

    heart_rate_1_min_value = models.CharField(max_length=10, null=True, blank=True)
    heart_rate_1_min_slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], null=True,
                                                blank=True)
    muscle_tone_1_min_value = models.CharField(max_length=100, null=True, blank=True)
    muscle_tone_1_min_slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], null=True,
                                                 blank=True)
    reflex_1_min_value = models.CharField(max_length=100, null=True, blank=True)
    reflex_1_min_slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], null=True,
                                            blank=True)
    colour_1_min_value = models.CharField(max_length=100, null=True, blank=True)
    colour_1_min_slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], null=True,
                                            blank=True)
    respiratory_effort_1_min_value = models.CharField(max_length=100, null=True, blank=True)
    respiratory_effort_1_min_slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)],
                                                        null=True, blank=True)

    heart_rate_5_min_value = models.CharField(max_length=10, null=True, blank=True)
    heart_rate_5_min_slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], null=True,
                                                blank=True)
    muscle_tone_5_min_value = models.CharField(max_length=100, null=True, blank=True)
    muscle_tone_5_min_slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], null=True,
                                                 blank=True)
    reflex_5_min_value = models.CharField(max_length=100, null=True, blank=True)
    reflex_5_min_slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], null=True,
                                            blank=True)
    colour_5_min_value = models.CharField(max_length=100, null=True, blank=True)
    colour_5_min_slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], null=True,
                                            blank=True)
    respiratory_effort_5_min_value = models.CharField(max_length=100, null=True, blank=True)
    respiratory_effort_5_min_slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)],
                                                        null=True, blank=True)

    class Meta:
        managed = False
        db_table = "maternity_extended_deliveryrecord"
        app_label = 'prescription'
