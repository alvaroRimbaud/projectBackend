from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # email = models.CharField(max_length=30)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # password = models.CharField(max_length=30)
    birthdate = models.DateField(null=True, blank=True)

    
    def __str__(self):
        return self.username
    