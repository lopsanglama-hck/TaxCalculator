from django.db import models

# Create your models here.
class Tax(models.Model):
    salary = models.IntegerField()
    allowance = models.IntegerField()
    bonus = models.IntegerField()
    others = models.IntegerField()
