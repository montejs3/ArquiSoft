# Generated by Django 3.2.6 on 2023-03-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=100)),
                ('fechaNacimiento', models.CharField(max_length=100)),
            ],
        ),
    ]
