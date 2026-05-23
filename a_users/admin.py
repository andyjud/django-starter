from allauth.account.models import EmailAddress
from allauth.account.admin import EmailAddressAdmin as AllauthEmailAddressAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from unfold.admin import ModelAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin, ModelAdmin):
    fieldsets = () + UserAdmin.fieldsets  # type: ignore

    fieldsets = (
        (None, {'fields': ('display_name', 'image',  'info')}),
    ) + UserAdmin.fieldsets  # type: ignore


# Unregister the default Allauth admin
try:
    admin.site.unregister(EmailAddress)
except admin.sites.NotRegistered:
    pass


# Re-register it with Unfold
@admin.register(EmailAddress)
class CustomEmailAddressAdmin(AllauthEmailAddressAdmin, ModelAdmin):
    search_fields = ["email", "user__username", "user__email"]
