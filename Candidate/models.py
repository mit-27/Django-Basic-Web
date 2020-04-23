from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.core.validators import RegexValidator
# Create your models here.


class Candidate(models.Model):
    # user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING)
    candidate_id = models.AutoField(primary_key=True)
    candidate_address = models.TextField(max_length=10,null=True, blank=True)
    # https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    candidate_phone = models.CharField(validators=[
                                       phone_regex], max_length=10, null=True, blank=True,unique=True)  # validators should be a list
    candidate_email = models.EmailField(null=True, blank=True,unique=True)
    candidate_name = models.CharField(max_length=50,unique=True,null=True, blank=True)
    candidate_gender = models.CharField(
        max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default='M')
    candidate_job_title = models.CharField(
        max_length=5, choices=[('jt1', "Developer"), ('jt2', "Tester")], default='jt1')
    candidate_source = models.CharField(
        max_length=5, choices=[('s1', 'Linkdln'), ('s2', 'Website')], default='s1')
    candidate_recruiter = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.candidate_name

    class Meta:
        managed = True
        db_table = 'candidate'
