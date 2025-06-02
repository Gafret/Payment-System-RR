import logging
from typing import Union

from django.core.exceptions import ValidationError
from django.db import transaction, IntegrityError

from orgs.models import Organization
from orgs.selectors import get_org_by_inn
from payments.models import Payment

logger = logging.getLogger(__name__)


@transaction.atomic
def create_payment(
    *, operation_id: str, amount: float, payer_inn: str, document_number: str, document_date: str
) -> Union[Payment, None]:

    org = get_org_by_inn(payer_inn)
    if org is None:
        # We register organisation forcefully because if we get
        # some invoice, there is an intention to notify us about
        # it, we'd rather have a record than not (esp. since inn isn't confidential)
        try:
            org = Organization.objects.create(inn=payer_inn)
            logger.info(f"В базу внесена новая компания/физ.лицо {payer_inn}")
        except IntegrityError as e:
            raise ValidationError("Неверный формат данных организации")

    try:
        payment = Payment.objects.create(
            id=operation_id,
            amount=amount,
            payer_inn=org,
            document_number=document_number,
            document_date=document_date,
        )
        logging.info(f"Пополнен баланс {org} на {amount}")
    except IntegrityError as e:
        cause = e.args[0]
        if cause == 1062:  # duplicate id
            return
        elif cause == 3819:  # bad request data for payment
            raise ValidationError("Неверный формат платежа")
        raise e

    return payment
