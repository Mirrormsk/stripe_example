# Generated by Django 5.0 on 2023-12-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0011_rename_rate_tax_percentage_tax_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="tax",
        ),
        migrations.AddField(
            model_name="order",
            name="tax_rates",
            field=models.ManyToManyField(to="payments.tax"),
        ),
    ]
