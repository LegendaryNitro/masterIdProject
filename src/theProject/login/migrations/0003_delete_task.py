# Generated by Django 3.2.8 on 2021-10-30 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_admin_panel_applicationid_applicationpassport_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
