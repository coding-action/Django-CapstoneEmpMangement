# Generated by Django 3.1.7 on 2021-04-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20210426_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='checkgender',
            field=models.CharField(default='Not Mentioned', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nationality',
            field=models.BooleanField(),
        ),
    ]
