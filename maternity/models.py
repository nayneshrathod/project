from django.db import models


# Create your models here.


class MaternityDetails(models.Model):
    hospital_id = models.IntegerField(blank=True, null=True)
    booking_id = models.CharField(max_length=110, blank=True, null=True)
    patient_id = models.IntegerField()
    preg_no = models.IntegerField()
    patient_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    active_medical_issues = models.TextField()
    active_pregnancy_issues = models.TextField()
    partner_name = models.CharField(max_length=255)
    partner_contact = models.CharField(max_length=255)
    partner_user_id = models.IntegerField()
    delivery_hospital_id = models.IntegerField()
    delivery_hospital_name = models.CharField(max_length=255)
    hospital_reg_number = models.CharField(max_length=251)
    lnmp_date = models.DateField()
    conception_date = models.DateField()
    expected_date_of_delivery = models.DateField()
    current_gestation = models.IntegerField()
    folloupdate = models.DateField()
    created_date = models.DateTimeField()
    created_by = models.IntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maternity_details'
