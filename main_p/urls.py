
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

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

urlpatterns = ([
    path('secret/place/of/admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/social/', include('allauth.socialaccount.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls', namespace='rest_framework_social_oauth2')),

    path('api/', include('blog.urls')),  # Include blog app URLs
    # chat/communities
    path('api/chat/', include('chat.urls')),
    # consultation
    path('api/consultation/', include('consultation.urls')),
    path('api/moderators/', include('moderators.urls')),
    

    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # REST Framework Browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Swagger documentation
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
    + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
