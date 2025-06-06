# Generated by Django 4.2.17 on 2025-06-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="payment",
            constraint=models.CheckConstraint(
                check=models.Q(("amount__gt", 0)), name="positive_amount"
            ),
        ),
    ]
