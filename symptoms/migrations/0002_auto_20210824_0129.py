# Generated by Django 3.2.6 on 2021-08-23 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_remove_doctor_work'),
        ('symptoms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptoms',
            name='specialit',
        ),
        migrations.AddField(
            model_name='symptoms',
            name='specialist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='doctor.specialist'),
            preserve_default=False,
        ),
    ]
