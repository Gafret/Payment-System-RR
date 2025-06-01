from typing import Union

from orgs.models import Organization


def get_org_by_inn(inn: str) -> Union[Organization, None]:
    try:
        org = Organization.objects.get(inn=inn)
    except Organization.DoesNotExist:
        return None

    return org
