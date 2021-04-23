from django.db import models
from django import forms

# Create your models here.
class Employee(models.Model):  
    FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]
    gender = (('MALE','MALE'),
         ('FEMALE','FEMALE'),)
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15) 
    category = models.CharField(max_length=15, choices=FRUIT_CHOICES, null=True)    
    #male = models.BooleanField(null=False)
    #female = models.BooleanField(null=False)
    checkgender = models.CharField(max_length=15,choices=gender, default='MALE')
    class Meta:  
        db_table = "employee"

