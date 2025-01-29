from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField()
    user = models.OneToOneField(
        "User", on_delete=models.CASCADE, related_name="account"
    )

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class User(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    suffix = models.CharField(max_length=255, blank=True)
    gender = models.PositiveSmallIntegerField()
    birth_date = models.DateField()
