from django.db import models

# Create your models here.
from django.db import models
from patient.models.models import Patient

class IPDRegistration(models.Model):
    admission_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField()
    ward = models.CharField(max_length=50)
    bed_number = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.admission_id} - {self.patient.FirstName} {self.patient.LastName}"

class IPDDeposit(models.Model):
    deposit_id = models.AutoField(primary_key=True)
    admission = models.ForeignKey(IPDRegistration, on_delete=models.CASCADE)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_date = models.DateField()
    def __str__(self):
        return f"{self.deposit_id} - {self.admission.patient.FirstName} {self.admission.patient.LastName}"

class IPDDischarge(models.Model):
    discharge_id = models.AutoField(primary_key=True)
    admission = models.ForeignKey(IPDRegistration, on_delete=models.CASCADE)
    discharge_date = models.DateField()
    discharge_summary = models.TextField()

class IPDAdmitReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    admission = models.ForeignKey(IPDRegistration, on_delete=models.CASCADE)
    report_details = models.TextField()

class IPDDepositReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    deposit = models.ForeignKey(IPDDeposit, on_delete=models.CASCADE)
    report_details = models.TextField()

class IPDDischargeReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    discharge = models.ForeignKey(IPDDischarge, on_delete=models.CASCADE)
    report_details = models.TextField()

class DepartmentReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=50)
    data_details = models.TextField()

class WardWiseReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    ward = models.CharField(max_length=50)
    data_details = models.TextField()

class DoctorWiseReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    doctor_id = models.CharField(max_length=20)
    data_details = models.TextField()

class TPAReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    tpa_id = models.CharField(max_length=20)
    transaction_details = models.TextField()
