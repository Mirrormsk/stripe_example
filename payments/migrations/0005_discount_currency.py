# Generated by Django 5.0 on 2023-12-25 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0004_rename_amount_discount_amount_off"),
    ]

    operations = [
        migrations.AddField(
            model_name="discount",
            name="currency",
            field=models.CharField(
                blank=True, max_length=3, null=True, verbose_name="валюта"
            ),
        ),
    ]
