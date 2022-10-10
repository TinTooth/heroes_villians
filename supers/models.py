from tkinter import CASCADE
from super_types.models import SuperType
from django.db import models

# Create your models here.
class Supers(models.Model):
    name = models.CharField(max_length = 255)
    alter_ego = models.CharField(max_length = 255)
    primary_ability = models.CharField(max_length = 255)
    secondary_ability = models.CharField(max_length = 255)
    super_typ = models.ForeignKey(SuperType, on_delete = CASCADE)

    