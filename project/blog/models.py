from django.db import models


# Create your models here.

class Parent(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey(to=Parent, null=True, on_delete=models.SET_NULL)
