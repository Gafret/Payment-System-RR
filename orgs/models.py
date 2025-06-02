from django.db import models
from django.db.models import CheckConstraint, Q


class Organization(models.Model):
    """
    Represents some organization or individual

    Fields:
        inn: individual tax number for company/individual

    Properties:
        balance: returns account balance of the company/individual
    """

    # 12 chars limit to include individuals
    inn = models.CharField(
        primary_key=True,
        editable=False,
        max_length=12,
        verbose_name="ИНН",
    )

    @property
    def balance(self):
        """Current company's balance"""
        sum = self.payments.aggregate(models.Sum("amount"))["amount__sum"]
        return sum

    def __str__(self):
        return self.inn

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
        constraints = [
            CheckConstraint(
                check=Q(inn__length=10) | Q(inn__length=12),
                name="inn_length",
            )
        ]
