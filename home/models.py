from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
MALE = "MALE"
FEMALE = "FEMALE"

GENDER = (
    (0, MALE),
    (1, FEMALE)
)

class User(AbstractUser):
    is_voter = models.BooleanField(default=True)
    gender = models.CharField(max_length=10,choices=GENDER, blank=False, null=False)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)