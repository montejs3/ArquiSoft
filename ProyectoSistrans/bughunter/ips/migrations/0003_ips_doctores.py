# Generated by Django 3.2.6 on 2023-04-15 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_remove_doctor_ips'),
        ('ips', '0002_ips_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='ips',
            name='doctores',
            field=models.ManyToManyField(to='doctor.Doctor'),
        ),
    ]
