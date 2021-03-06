# Generated by Django 3.1.7 on 2021-04-26 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='', upload_to='images/')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
                ('experience', models.IntegerField(default='0')),
                ('category', models.CharField(choices=[('HR Management Software', 'HR Management Software'), ('Cloud & SaaS', 'Cloud & SaaS'), ('CMMS-Software', 'CMMS Software'), ('Telecommunications Management', 'Telecommunications Management'), ('ERP-Software', 'ERP Software')], max_length=100, null=True)),
                ('address', models.TextField(default='null')),
                ('dob', models.DateField(default='1990-01-05')),
                ('checkgender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=15)),
                ('nationality', models.BooleanField(default='False')),
                ('salary', models.FloatField(default='00.00')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
