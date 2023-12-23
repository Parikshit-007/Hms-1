from django.db import models

class Patient(models.Model):
    PatientID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    DOB = models.DateField()
    Gender = models.CharField(max_length=10)
    ContactNumber = models.CharField(max_length=15)
    Address = models.TextField()
    Email = models.EmailField()

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
