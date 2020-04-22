from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, blank=True, null=True)



class Disease(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='diseases')


class Habit(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='habits')


class Health(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='healths')
