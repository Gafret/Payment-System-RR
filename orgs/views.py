from django.http import HttpRequest, JsonResponse, HttpResponse

from orgs.selectors import get_org_by_inn


def get_org_balance(request: HttpRequest, inn: str):
    if request.method == "GET":
        inn_len = len(inn)
        if inn_len != 10 and inn_len != 12:
            return JsonResponse({"msg": "Неверный формат ИНН"})

        org = get_org_by_inn(inn)

        if org is None:
            return JsonResponse({"msg": "Такой организации нет"}, status=404)

        balance = org.balance.get("amount__sum", "null")

        return JsonResponse({
            "inn": org.inn,
            "balance": balance
        }, status=200)

    return HttpResponse(status=405)
