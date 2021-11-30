from django.db import models
from django.utils.timezone import now
import uuid
import datetime

class Company(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField( null=True, )
    url = models.CharField(null=False, max_length=100)
    city = models.CharField(null=False, max_length=255)
    address = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.TextField()
    status = models.IntegerField(default=0)
    last_login_at = models.DateTimeField(null=True)
    last_ip_address = models.TextField(null=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(null=True)

    # class Meta:
        # managed = False
        # db_table = "uasdser"

    def __str__(self):
        return self.name

class Session(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING)
    expired_at = models.DateTimeField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
