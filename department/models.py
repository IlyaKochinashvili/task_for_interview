from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    department_code = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_mane = models.CharField(max_length=128, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)
    is_stuff = models.BooleanField(default=False, null=True, blank=True)
    departament = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.phone_number
