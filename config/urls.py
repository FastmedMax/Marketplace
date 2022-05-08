from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views import UserViewSet


router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

schema_view = get_schema_view(
    openapi.Info(title="Marketplace Api", default_version="v1"),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('api.urls', namespace='api')),
    path("api/auth/", include(router.urls)),
    path("api/auth/", include('djoser.urls.authtoken')),
    path(
        "redoc/",
        login_required(
            TemplateView.as_view(
                template_name="redoc.html",
            )
        )
    )
]
