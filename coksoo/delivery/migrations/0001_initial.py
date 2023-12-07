# Generated by Django 4.2.4 on 2023-12-07 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("restaurant", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Delivery",
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
                ("date", models.DateField()),
                ("address", models.CharField(max_length=600)),
                ("comment", models.TextField()),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "Option One"),
                            (2, "Option Two"),
                            (3, "Option Three"),
                        ]
                    ),
                ),
                ("number_of_foods", models.IntegerField(default=0)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_delivery",
                        to="user.client",
                    ),
                ),
                (
                    "cook",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.cook",
                    ),
                ),
                (
                    "courier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="courier_delivery",
                        to="user.courier",
                    ),
                ),
            ],
            options={
                "permissions": [
                    ("change_cook_delivery", "Can change the cook of the delivery")
                ],
            },
        ),
        migrations.CreateModel(
            name="DeliveryMeal",
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
                    "delivery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="delivery.delivery",
                    ),
                ),
                (
                    "meal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurant.meal",
                    ),
                ),
            ],
        ),
    ]
