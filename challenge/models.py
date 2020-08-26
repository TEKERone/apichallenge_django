from django.db import models

class Challenge(models.Model):
    name = models.CharField(max_length=55, blank=False)    
    value = models.FloatField(null=False, blank=False)
    discount_value = models.FloatField(null=True, blank=False)
    stock = models.IntegerField(default=0)
    

