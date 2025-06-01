from django.contrib import admin

from payments.models import Payment


class PaymentAdmin(admin.ModelAdmin):
    search_fields = ["payer_inn", "document_number"]
    list_display = ["payer_inn", "document_number", "amount", "document_date"]


admin.site.register(Payment, PaymentAdmin)
