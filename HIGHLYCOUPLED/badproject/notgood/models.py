from django.db import models


class Customer(models.Model):
    ssn = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)


class Application(models.Model):
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
