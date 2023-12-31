# Generated by Django 5.0 on 2023-12-25 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "percentage",
                    models.DecimalField(
                        decimal_places=2, max_digits=6, verbose_name="процент скидки"
                    ),
                ),
            ],
            options={
                "verbose_name": "скидка",
                "verbose_name_plural": "скидки",
            },
        ),
        migrations.CreateModel(
            name="Tax",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rate",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="размер"
                    ),
                ),
            ],
            options={
                "verbose_name": "налог",
                "verbose_name_plural": "налоги",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="создан"),
                ),
                (
                    "discount",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="payments.discount",
                    ),
                ),
                ("items", models.ManyToManyField(to="items.item")),
                (
                    "tax",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="payments.tax",
                    ),
                ),
            ],
            options={
                "verbose_name": "заказ",
                "verbose_name_plural": "заказы",
            },
        ),
    ]
