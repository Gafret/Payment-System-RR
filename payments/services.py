import logging
from typing import Union

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
        logger.info("В базу внесена новая компания/физ.лицо")
        org = Organization.objects.create(inn=payer_inn)

    try:
        payment = Payment.objects.create(
            id=operation_id,
            amount=amount,
            payer_inn=org,
            document_number=document_number,
            document_date=document_date,
        )
        logging.info(f"Пополнен баланс", extra={"org": org, "amount": amount})
    except IntegrityError as e:
        logging.error("Данная операция уже была проведена", extra={"err": e})
        return

    return payment
