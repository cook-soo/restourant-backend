# Generated by Django 4.2.4 on 2023-12-07 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_remove_cook_qr_code"),
        ("delivery", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="cook",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.cook",
            ),
        ),
        migrations.AlterField(
            model_name="delivery",
            name="courier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="courier_delivery",
                to="user.courier",
            ),
        ),
    ]