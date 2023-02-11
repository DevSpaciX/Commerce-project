# Generated by Django 4.1.6 on 2023-02-11 13:42

from django.core.management import call_command
from django.db import migrations


def load_fixtures(state, schema_editor):
    call_command("loaddata", "fixture_file.json")


def reverse_load_fixtures(state, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('pateik_app', '0003_alter_payment_day_alter_payment_time_and_more'),
    ]

    operations = [
        migrations.RunPython(load_fixtures, reverse_load_fixtures)
    ]