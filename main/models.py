from django.db import models

class Subsidiary(models.Model):
    name = models.CharField(max_length=100)
    billing_name = models.CharField(max_length=100, null=True, blank=True)
    rut = models.CharField(max_length=12, null=True, blank=True)
    business_activity = models.CharField(max_length=1000, null=True, blank=True)
    logo = models.ImageField(upload_to="logos/", null=True, blank=True)
    

    def __str__(self) -> str:
        return self.name