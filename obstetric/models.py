from django.db import models


# Create your models here.

class ObstetricForm(models.Model):
    TERATOGENS = (
        ("Herpes", "Herpes"),
        ("Hepatitis", "Hepatitis"),
        ("Rubella", "Rubella"),
        ("Varicella", "Varicella"),
        ("Syphillis", "Syphillis"),
        ("Toxoplasmosis", "Toxoplasmosis"),
        ("CMV", "CMV"),
        ("Alcohol", "Alcohol"),
        ("Tobacco", "Tobacco"),
        ("Cocaine", "Cocaine"),
        ("Aminopterin", "Aminopterin"),
        ("Androgens", "Androgens"),
        ("Busulfan (Myleran)", "Busulfan (Myleran)"),
        ("Carbamazepine (Tegretol)", "Carbamazepine (Tegretol)"),
        ("Chlorobiphenyls", "Chlorobiphenyls"),
        ("Coumarins", "Coumarins"),
        ("Warfarin (Coumadin)", "Warfarin (Coumadin)"),
        ("Cyclophosphamide (Cytoxan)", "Cyclophosphamide (Cytoxan)"),
        ("Danazol (Danocrine)", "Danazol (Danocrine)"),
        ("Diethylstilbestrol (Des)", "Diethylstilbestrol (Des)"),
        ("Etretinate (Tegison)", "Etretinate (Tegison)"),
        ("Isotretinoin (Accutane)", "Isotretinoin (Accutane)"),
        ("Lead","Lead"),
        ("Lithium (Eskalith)","Lithium (Eskalith)"),
        ("Mercury","Mercury"),
        ("Methimazole (Tapazole)","Methimazole (Tapazole)"),
        ("Methotrexate (Rheumatrex)","Methotrexate (Rheumatrex)"),
        ("Penicillamine (Depen, Cuprimine)","Penicillamine (Depen, Cuprimine)"),
        ("Phenytoin (Dilantin)","Phenytoin (Dilantin)"),
        ("Phenobarbital (Solfoton)","Phenobarbital (Solfoton)"),
        ("Propylthiouracil (Ptu)","Propylthiouracil (Ptu)"),
        ("Prostaglandins","Prostaglandins"),
        ("Radioactive Iodine","Radioactive Iodine"),
        ("Tetracycline (Sumycin)","Tetracycline (Sumycin)"),
        ("rimethadione (Tridione)","rimethadione (Tridione)"),
        ("Valproic Acid (Depakene)","Valproic Acid (Depakene)"),
    )

    STDS = (
        ("HIV","HIV"),
        ("Hepatitis B","Hepatitis B"),
        ("Syphilis", "Syphilis"),
        ("Gonorrhea", "Gonorrhea"),
        ("Trichomoniasis", "Trichomoniasis"),
    )

    user_id = models.IntegerField(blank=True, null=True)
    hospital_id = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    phone_no = models.CharField(max_length=12, blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    hypertension = models.CharField(max_length=100, blank=True, null=True)
    diabetes = models.CharField(max_length=100, blank=True, null=True)
    sexually_transmitted_disease = models.CharField(max_length=100, blank=True, null=True)
    pyelonephritis_uti = models.CharField(max_length=100, blank=True, null=True, choices=STDS)
    acute_surgical_problem = models.CharField(max_length=100, blank=True, null=True)
    genital_tract_abnormalities = models.CharField(max_length=100, blank=True, null=True)
    maternal_age = models.IntegerField()
    maternal_weight = models.FloatField()
    maternal_height = models.FloatField()
    exposure_of_teratogens = models.CharField(max_length=100, blank=True, null=True)
    exposure_to_mercury = models.CharField(max_length=100, blank=True, null=True)
    prior_stillbirth = models.IntegerField(blank=True, null=True)
    prior_preterm_delivery = models.IntegerField(blank=True, null=True)
    prior_neonate_with_genitic_or_congenital_disorder = models.TextField(blank=True, null=True)
    polyhydramnios_and_oligohydramnios = models.CharField(max_length=100, blank=True, null=True)
    multifetal_pregnancy = models.IntegerField(blank=True, null=True)
    prior_birth_injury = models.TextField(blank=True, null=True)
    gravidity_and_parity = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'prescription'
        db_table = 'obstetric_form' 

class ObstetricPhysicalExamination(models.Model):
    obstetric = models.ForeignKey(ObstetricForm, on_delete=models.CASCADE)
    lesions_or_discharge = models.CharField(max_length=100)
    colour_and_consistency_of_cervix = models.CharField(max_length=100)
    cervical_samples_for_testing = models.CharField(max_length=100, blank=True, null=True)
    pelvic_capacity = models.CharField(max_length=100)
    blood_pressure = models.CharField(max_length=100)
    weight = models.FloatField()
    uterine_size = models.CharField(max_length=100, blank=True, null=True)
    fundal_weight = models.FloatField()
    fetal_heart_rate_and_activity = models.CharField(max_length=100)
    maternal_diet = models.TextField()
    weight_gain = models.FloatField()
    date_of_examination = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    visit_no = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    modified_by = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'prescription'
        db_table = 'obstetric_physical_examination'
