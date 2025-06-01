import json

from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from payments.services import create_payment


@csrf_exempt
def handle_payment_request(request: HttpRequest):
    if request.method == "POST":
        payment_data = json.loads(request.body)

        try:
            create_payment(**payment_data)
        except TypeError:
            return HttpResponse(status=400)

        return HttpResponse(status=200)

    return HttpResponse(status=405)
