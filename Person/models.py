from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

USER_TYPE = (
    (0, 'Admin'),
    (1, 'Person')
)
GENDER = (
    (0, 'Male'),
    (1, 'Female')
)


class Person(models.Model):
    name = models.CharField(max_length=240, blank=True, null=True)
    username = models.CharField(max_length=240, blank=True, null=True)
    password = models.CharField(max_length=100)
    user_type = models.IntegerField(choices=USER_TYPE)
    email = models.EmailField()
    gender = models.IntegerField(choices=GENDER)
    birthdate = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True, blank=True)
    disease = models.ManyToManyField('Disease', related_name='people', blank=True)
    habit = models.ManyToManyField('Habit', related_name='people', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Person'


class Disease(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Disease'


class Habit(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Habit'


############Address########

class Address(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    district = models.ForeignKey('District', on_delete=models.CASCADE, null=True)
    street = models.ForeignKey('Street', on_delete=models.CASCADE, null=True)
    building = models.ForeignKey('Building', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.region} + '

    class Meta:
        db_table = 'Address'


# @receiver(post_save, sender=Address)
# def wtf(sender, instance, created, **kwargs):
#     slug = slugify(instance.name)
#     name = slug
#     up = Address(name=name)
#     up.save()


class Region(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Region'


class City(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'City'


class District(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'District'


class Street(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='streets')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Street'


class Building(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='buildings')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Building'


class Busyness(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Busyness'


class Job(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Job'
