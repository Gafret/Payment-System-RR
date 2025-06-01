from django.urls import path

from orgs.views import get_org_balance

urlpatterns = [
    path("organizations/<str:inn>/balance/", get_org_balance, name="org-balance"),
]
