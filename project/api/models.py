from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField( null=True, )
    url = models.CharField(null=False, max_length=100)
    city = models.CharField(null=False, max_length=255)
    address = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.name


    # name = models.CharField(max_length=50, unique=True)
    # description = models.TextField(null=False, blank=False)
    # url = models.CharField(max_length=100)
    # city = models.CharField(max_length=255)
    # address = models.CharField(max_length=255)