# Generated by Django 4.2.8 on 2024-05-15 01:04

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="country",
            field=django_countries.fields.CountryField(default="", max_length=2),
        ),
    ]
