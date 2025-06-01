from orgs.models import Organization


def get_org_by_inn(inn: str) -> Organization:
    return Organization.objects.get(inn=inn)
