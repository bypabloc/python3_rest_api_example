from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name