# Generated by Django 3.1.7 on 2021-04-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_auto_20210427_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='category',
            field=models.CharField(choices=[('HR Management Software', 'HR Management Software'), ('Cloud & SaaS', 'Cloud & SaaS'), ('CMMS Software', 'CMMS Software'), ('Telecomm Management', 'Telecommunications Management'), ('ERP Software', 'ERP Software')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nationality',
            field=models.BooleanField(default=True),
        ),
    ]
