# Generated by Django 5.0 on 2023-12-25 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0006_remove_order_discount_order_discount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="discount",
        ),
        migrations.AddField(
            model_name="order",
            name="discount",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="payments.discount",
            ),
        ),
    ]
