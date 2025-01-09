# Create your models here.
from django.db import models
class Country(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    sortname = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    phonecode = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class State(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name