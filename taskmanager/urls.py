from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated

# Define the schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Task Management API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[IsAuthenticated],
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('api/', include('task.urls')),  # Include task app's URLs under "api/"

    # Swagger UI documentation endpoint
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Optional: JSON schema endpoint
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
