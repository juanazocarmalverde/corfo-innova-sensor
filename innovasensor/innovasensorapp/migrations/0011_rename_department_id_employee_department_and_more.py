# Generated by Django 4.2.16 on 2024-10-06 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('innovasensorapp', '0010_rename_employee_id_sensorchart_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='department_id',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='role_id',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='fail_id',
            new_name='fail',
        ),
        migrations.RenameField(
            model_name='sensorchart',
            old_name='requirement_id',
            new_name='requirement',
        ),
    ]
