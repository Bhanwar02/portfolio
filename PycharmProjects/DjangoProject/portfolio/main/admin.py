from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "message",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
    )

    list_filter = (
        "created_at",
    )

    def short_message(self, obj):
        return obj.message[:40]