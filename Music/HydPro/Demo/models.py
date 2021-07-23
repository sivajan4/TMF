from django.db import models
from pgcrypto import fields
# Create your models here.

class Person(models.Model):
    email = fields.EmailPGPSymmetricKeyField()
    salary = fields.IntegerPGPSymmetricKeyField()

    def __str__(self):
        return self.email
class Details(models.Model):
    person = models.ForeignKey(Person,blank=True,null=True, on_delete=models.SET_NULL)
    name = fields.CharPGPSymmetricKeyField(max_length=150)
    address = fields.TextPGPSymmetricKeyField()

    def __str__(self):
        return self.name

#publications = models.ManyToManyField(Publication)
class Designation(models.Model):
    designation = fields.CharPGPSymmetricKeyField(max_length=150)
    person = models.ManyToManyField(Person)

    def __str__(self):
        return self.designation
