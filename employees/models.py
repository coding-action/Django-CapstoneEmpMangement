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
    profile_pic = models.ImageField(upload_to='images/',default="")
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15) 
    category = models.CharField(max_length=45, choices=CATEGORY_CHOICES, null=True) 
    addresses = models.TextField(default="null")
    dob = models.DateField(default='1990-01-05')
    checkgender = models.CharField(max_length=15,choices=gender, default='MALE')
    nationality =  models.BooleanField(default='False')
    salary = models.FloatField(default='00.00')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    class Meta:  
        db_table = "employee"

