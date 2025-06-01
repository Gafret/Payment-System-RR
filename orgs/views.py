from django.http import HttpRequest, JsonResponse, HttpResponse

from orgs.models import Organization
from orgs.selectors import get_org_by_inn


def get_org_balance(request: HttpRequest, inn: str):
    if request.method == "GET":
        try:
            org = get_org_by_inn(inn)
        except Organization.DoesNotExist:
            return JsonResponse({"msg": "Такой организации нет"}, status=404)

        balance = org.balance

        return JsonResponse({
            "inn": org.inn,
            "balance": balance
        }, status=200)

    return HttpResponse(status=405)
