from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from Users.models import User
from Users.forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email', 'is_active']
    list_filter = ['is_admin']
    fieldsets = [
        (None, {'fields': ('email', 'password')}),
        ("Telegram", {"fields": ('telegram_id',)}),
        ("Permissions", {"fields": ("is_admin", 'is_active')}),
    ]
    add_fieldsets = [
        (None, {'fields': ('email', 'password1', 'password2'), 'classes': ['wide']})
    ]

    search_fields = ['email']
    ordering = ['id', 'email']
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
