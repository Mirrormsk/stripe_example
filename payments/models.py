from django.db import models

from items.models import Item

NULLABLE = {"null": True, "blank": True}


class Discount(models.Model):
    percent_off = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="процент скидки", default=0
    )
    amount_off = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="сумма скидки", default=0
    )
    currency = models.CharField(max_length=3, verbose_name="валюта")

    class Meta:
        verbose_name = "скидка"
        verbose_name_plural = "скидки"

        constraints = [
            models.CheckConstraint(
                check=models.Q(percent_off__gte=0),
                name="percent_off_positive",
            ),
            models.CheckConstraint(
                check=models.Q(percent_off__lte=100),
                name="percent_off_max_value",
            ),
            models.CheckConstraint(
                check=models.Q(amount_off__gte=0),
                name="amount_off_positive",
            ),
        ]

    def save(self, *args, **kwargs):
        """Makes currency uppercase"""
        self.currency = self.currency.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f'{self.amount_off if self.amount_off else ""} '
            f'{self.currency if self.currency else ""}'
            f'{str(self.percent_off) + "%" if self.percent_off else ""}'
        )


class Tax(models.Model):
    percentage = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="размер"
    )
    display_name = models.CharField(max_length=20, verbose_name="название")
    inclusive = models.BooleanField(verbose_name="включен")
    description = models.TextField(verbose_name="описание", **NULLABLE)
    country = models.CharField(max_length=100, verbose_name="страна", **NULLABLE)

    class Meta:
        verbose_name = "налог"
        verbose_name_plural = "налоги"


class Order(models.Model):
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="создан")
    discounts = models.ManyToManyField(Discount)
    tax_rates = models.ManyToManyField(Tax)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return f"Order #{self.id} | {self.created_at}"

    @property
    def total_price(self):
        return sum(self.items.values_list("price", flat=True))
