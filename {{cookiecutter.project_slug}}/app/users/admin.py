from django.contrib import admin

from app.users.models import (
    BaseUser,
)


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'created_at')
    search_fields = ('email',)
    ordering = ('id',)
