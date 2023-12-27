from django.db import models

from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    RELATION_CHOICES = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sibling', 'Sibling'),
        ('Spouse', 'Spouse'),
        ('Friend', 'Friend'),
        ('Other', 'Other'),
    ]

    PatientID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    MiddleName = models.CharField(max_length=255, blank=True, null=True)
    LastName = models.CharField(max_length=255)
    Religion = models.CharField(max_length=255, blank=True, null=True)
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    Age = models.IntegerField(blank=True, null=True)
    DOB = models.DateField()
    Country = models.CharField(max_length=255, blank=True, null=True)
    State = models.CharField(max_length=255, blank=True, null=True)
    CityTaluka = models.CharField(max_length=255, blank=True, null=True)
    Address = models.TextField()
    PinCode = models.CharField(max_length=10, blank=True, null=True)
    Case = models.CharField(max_length=255, blank=True, null=True)
    ContactNumber = models.CharField(max_length=15)
    ReferredBy = models.CharField(max_length=255, blank=True, null=True)
    ConditionDuringArrival = models.TextField(blank=True, null=True)
    ModeOfArrival = models.CharField(max_length=255, blank=True, null=True)
    CareOfPerson = models.CharField(max_length=255, blank=True, null=True)
    BroughtBy = models.CharField(max_length=255, blank=True, null=True)
    RelationWithPatient = models.CharField(max_length=20, choices=RELATION_CHOICES, blank=True, null=True)
    Email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class PatientHistory(models.Model):
    HistoryID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    MedicalHistoryDetails = models.TextField()
    TreatmentDetails = models.TextField()

class PatientBilling(models.Model):
    BillingID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    InvoiceDetails = models.TextField()

class PatientLedger(models.Model):
    LedgerID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TransactionDetails = models.TextField()

class TreatmentInformation(models.Model):
    TreatmentID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TreatmentDetails = models.TextField()

class PatientReminder(models.Model):
    ReminderID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ReminderDetails = models.TextField()

class PatientVisitList(models.Model):
    VisitID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    VisitDate = models.DateField()
    Reason = models.TextField()
