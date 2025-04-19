from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

class City(models.Model):
    name = models.CharField(max_length=350)
    country = CountryField(blank_label="select country", blank=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}, {self.country if self.country else "No country"}"

class CustomUser(AbstractUser):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
