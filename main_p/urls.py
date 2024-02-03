from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="GlobalVibes Blog API",
        default_version='v1',
        description="Explore the world through the GlobalVibes blog. Engage with diverse content on various topics.",
        terms_of_service="https://www.globalvibesblog.com/terms/",
        contact=openapi.Contact(email="contact@globalvibesblog.com"),
        license=openapi.License(name="SemanticDev Licensed"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # Include blog app URLs
    path('accounts/', include('allauth.urls')),
    path('accounts/social/', include('allauth.socialaccount.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls', namespace='rest_framework_social_oauth2')),

    # REST Framework Browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Swagger documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
