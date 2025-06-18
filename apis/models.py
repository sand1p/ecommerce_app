from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.IntegerField(max_length=10, blank=True)
    # Todo: add roles = models  as a list field

