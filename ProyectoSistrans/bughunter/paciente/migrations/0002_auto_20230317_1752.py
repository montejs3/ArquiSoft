# Generated by Django 3.2.6 on 2023-03-17 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='name',
            new_name='namePaciente',
        ),
        migrations.AddField(
            model_name='paciente',
            name='documento',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='estatura',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='prioridadpaciente',
            field=models.CharField(default='baja', max_length=101),
        ),
        migrations.AddField(
            model_name='paciente',
            name='regimen',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='edad',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fechaNacimiento',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
