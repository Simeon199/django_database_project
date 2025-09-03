from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30) # Tabellenspalte
    last_name = models.CharField(max_length=30) # Tabellenspalte
    newsletter_abo = models.BooleanField(default=True)
    email_address = models.CharField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)