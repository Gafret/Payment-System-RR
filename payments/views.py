from django.http import HttpRequest, HttpResponse

from payments.services import create_payment


def handle_payment_request(request: HttpRequest):
    if request.method == "POST":
        payment_data = request.POST
        create_payment(**payment_data)

        return HttpResponse(status=200)

    return HttpResponse(status=405)
