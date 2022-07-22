# Generated by Django 4.0.6 on 2022-07-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern_form',
            name='FormStatus',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DEACTIVE', 'DEACTIVE')], default='ACTIVE', max_length=10),
        ),
        migrations.AlterField(
            model_name='internapplication',
            name='Status',
            field=models.CharField(choices=[('SHORTLISTED', 'shortlisted'), ('REJECTED', 'rejected'), ('PENDING', 'pending')], default='PENDING', max_length=20),
        ),
    ]