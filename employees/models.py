from django.db import models
from django import forms
import datetime

# Create your models here.
class Employee(models.Model):  
    CATEGORY_CHOICES= [
    ('HR Management Software', 'HR Management Software'),
    ('Cloud & SaaS', 'Cloud & SaaS'),
    ('CMMS Software', 'CMMS Software'),
    ('Telecomm Management', 'Telecommunications Management'),
    ('ERP Software', 'ERP Software')
    ]
    gender = (('Male','MALE'),
         ('Female','FEMALE'),)
    profile_pic = models.ImageField(upload_to='images/',default="")
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15) 
    experience = models.IntegerField(default='0')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True) 
    address = models.TextField(default="null")
    dob = models.CharField(max_length=100)
    checkgender = models.CharField(max_length=15,choices=gender, default='M')
    nationality =  models.BooleanField()
    salary = models.FloatField(default='00.00')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    class Meta:  
        db_table = "employee"

