from django.core.validators import MinLengthValidator
from django.db import models


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
        validators=[MinLengthValidator(10, "INN can't be shorter than 10")],
        verbose_name="ИНН",
    )

    @property
    def balance(self):
        """Current company's balance"""
        return self.payments.aggregate(models.Sum("amount"))

    def __str__(self):
        return self.inn

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
