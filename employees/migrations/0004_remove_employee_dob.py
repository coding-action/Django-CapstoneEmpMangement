# Generated by Django 3.1.7 on 2021-04-26 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20210426_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='dob',
        ),
    ]
