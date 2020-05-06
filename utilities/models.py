from django.db import models

class HospitalIpdPatient(models.Model):
    user_id = models.IntegerField()
    uhidno = models.CharField(max_length=100)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=40)
    email = models.TextField(blank=True, null=True)
    mlc = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    adharcard = models.CharField(max_length=110, blank=True, null=True)
    phone = models.CharField(max_length=110)
    relative_phoneno = models.CharField(max_length=200, blank=True, null=True)
    rpname = models.CharField(max_length=100, blank=True, null=True)
    relativename = models.CharField(max_length=100)
    remail = models.CharField(max_length=100, blank=True, null=True)
    rrelation = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=40)
    age = models.IntegerField()
    weight = models.IntegerField()
    blood_group = models.CharField(max_length=40, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    mlc_no = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    date_of_birth = models.CharField(max_length=500, blank=True, null=True)
    staff_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
    booking_type = models.IntegerField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hospital_ipd_patient'
        app_label = 'utilities'