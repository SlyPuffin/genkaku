# Generated by Django 4.2.5 on 2023-09-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hallucination", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sight",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/%vision_title/"
            ),
        ),
    ]