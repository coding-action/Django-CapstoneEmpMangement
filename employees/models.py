from django.db import models
from django import forms
import datetime

# Create your models here.
class Employee(models.Model):  
    CATEGORY_CHOICES= [
    ('HR Management Software', 'HR Management Software'),
    ('Cloud & SaaS', 'Cloud & SaaS'),
    ('CMMS Software', 'CMMS Software'),
    ('Telecommunications Management', 'Telecommunications Management'),
    ('ERP Software', 'ERP Software')
    ]
    gender = (('MALE','MALE'),
         ('FEMALE','FEMALE'),)

    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15) 
    category = models.CharField(max_length=45, choices=CATEGORY_CHOICES, null=True)  
  
    #male = models.BooleanField(null=False)
    #female = models.BooleanField(null=False)
    dob = models.DateField()
    address = models.TextField()
    checkgender = models.CharField(max_length=15,choices=gender, default='MALE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:  
        db_table = "employee"

