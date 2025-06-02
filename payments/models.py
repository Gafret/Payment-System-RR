from django.db import models
from django.db.models import Q
from django.db.models.constraints import CheckConstraint

from orgs.models import Organization


class Payment(models.Model):
    """
    Payment received by organization

    Fields:
        amount: sum of the payment
        payer_inn: inn of the organization receiving payment
        document_number: number of the document
        document_date: processing date
    """

    id = models.UUIDField(
        primary_key=True,
        editable=False,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма",
    )
    payer_inn = models.ForeignKey(
        Organization,
        related_name="payments",
        on_delete=models.DO_NOTHING,
        verbose_name="ИНН",
    )
    document_number = models.CharField(
        max_length=20,
        verbose_name="Номер документа",
    )
    document_date = models.DateTimeField(
        verbose_name="Дата документа",
    )

    def __str__(self):
        return f"{self.payer_inn} {self.document_number}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        constraints = [
            CheckConstraint(
                check=Q(amount__gt=0),
                name="positive_amount",
            )
        ]
