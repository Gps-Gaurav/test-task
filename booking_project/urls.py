from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token
from shared.views import LogoutView

schema_view = get_schema_view(
   openapi.Info(
      title="Booking API",
      default_version='v1',
      description="User availability and guest booking system",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/availability/', include('availability.urls')),
    path('api/book/', include('booking.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('accounts/logout/', LogoutView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
