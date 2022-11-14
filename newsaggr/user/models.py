from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField

class Profile(models.Model):
    email = models.EmailField(max_length=255,primary_key=True)
    arguments=PickledObjectField(null=True, blank=True)
    def __str__(self):
        return self.email