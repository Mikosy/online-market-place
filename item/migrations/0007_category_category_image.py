# Generated by Django 4.2.8 on 2024-06-05 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0006_alter_product_available"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="category_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="category_images/"
            ),
        ),
    ]
