from django.db import models

USER_TYPE = (
    (0, 'Admin'),
    (1, 'Person')
)


class Person(models.Model):
    name = models.CharField(max_length=240, blank=True, null=True)
    username = models.CharField(max_length=240, blank=True, null=True)
    password = models.CharField(max_length=100)
    user_type = models.IntegerField(choices=USER_TYPE)
    birthdate = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    disease = models.ManyToManyField('Disease', related_name='people', blank=True)
    habit = models.ManyToManyField('Habit', related_name='people', blank=True)
    health = models.ManyToManyField('Health', related_name='people', blank=True)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Habit(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Health(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


############Address########

class Address(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    district = models.ForeignKey('District', on_delete=models.CASCADE)
    street = models.ForeignKey('Street', on_delete=models.CASCADE)
    building = models.ForeignKey('Building', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    distrcit = models.ForeignKey(District, on_delete=models.CASCADE, related_name='streets')

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='buildings')

    def __str__(self):
        return self.name


class Busyness(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
