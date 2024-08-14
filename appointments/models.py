from django.conf import settings
from django.db import models
from django.utils import timezone

from common.models import AbstractBaseModel


class Doctor(AbstractBaseModel):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    # Ej. {'Monday': ['AM', 'PM'], 'Tuesday': ['AM']}
    available_days = models.JSONField()
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created = models.DateTimeField(
        default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.name} - {self.specialty}"


class Patient(AbstractBaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    primary_language = models.CharField(max_length=50)
    referred_by_physician = models.BooleanField(default=False)
    created = models.DateTimeField(
        default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(AbstractBaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    reason_for_appointment = models.TextField()
    interpretation_services = models.BooleanField(default=False)
    visit_type = models.CharField(max_length=20, choices=[(
        'In-office', 'In-office'), ('Virtual', 'Virtual'), ('Doesn\'t matter', 'Doesn\'t matter')])
    preferred_day = models.CharField(max_length=20, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), (
        'Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('First available', 'First available')])
    preferred_time = models.CharField(max_length=20, choices=[(
        'AM', 'AM'), ('PM', 'PM'), ('First available', 'First available')])
    payment_method = models.CharField(max_length=50, choices=[(
        'Insurance', 'Insurance'), ('Out-of-pocket', 'Out-of-pocket')])
    insurance_company = models.CharField(max_length=255, blank=True, null=True)
    insurance_product_type = models.CharField(
        max_length=50, blank=True, null=True)
    insurance_policy_number = models.CharField(
        max_length=50, blank=True, null=True)
    insurance_policy_holder = models.CharField(
        max_length=50, blank=True, null=True)
    created = models.DateTimeField(
        default=timezone.now, editable=False)

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.name} for {self.patient.first_name} {self.patient.last_name}"
