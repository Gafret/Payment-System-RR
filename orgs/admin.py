from django.contrib import admin

from orgs.models import Organization


class OrgAdmin(admin.ModelAdmin):
    search_fields = ["inn"]


admin.site.register(Organization, OrgAdmin)
