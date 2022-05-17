from django.contrib import admin

from .models import User, UserProduct, Product, ProductRate


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = (
        "password", "groups", "is_active",
        "is_staff", "is_superuser", "last_login",
        "date_joined", "user_permissions"
    )
