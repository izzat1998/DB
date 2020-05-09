from django.db import models

# Create your models here.
from Person.models import Person


class Statistics(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    walking_meters_per_day = models.FloatField(null=True, blank=True)
    avg_num_of_cigarettes_per_day = models.FloatField(null=True, blank=True)
    avg_amount_of_alcohol_per_day = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.person.username} + {self.id}'

    class Meta:
        db_table = 'Statistics'
