from django.contrib import admin

from .models import User, Category, UserProduct, Product, ProductImage, ProductRate


admin.site.register(Category)


class UserProductAdminInline(admin.StackedInline):
    model = UserProduct
    classes = ["collapse"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (UserProductAdminInline,)
    exclude = (
        "password", "groups", "is_active",
        "is_staff", "is_superuser", "last_login",
        "date_joined", "user_permissions"
    )


class ProductRateAdminInline(admin.StackedInline):
    model = ProductRate
    classes = ["collapse"]


class ProductImageAdminInline(admin.StackedInline):
    model = ProductImage
    classes = ["collapse"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductRateAdminInline, ProductImageAdminInline)
