from django.urls import path

from payments.views import handle_payment_request

urlpatterns = [
    path("webhook/bank/", handle_payment_request, name="handle-payment"),
]
