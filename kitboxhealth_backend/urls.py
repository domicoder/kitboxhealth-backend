from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from appointments.views import (AppointmentViewSet, CustomAuthToken,
                                DoctorViewSet, LogoutView, PatientViewSet,
                                UserRegistrationView)

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/doctors/by-specialty/<str:specialty>/',
         DoctorViewSet.as_view({'get': 'by_specialty'}), name='doctors-by-specialty'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
    path('api/auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/sign-up/', UserRegistrationView.as_view(),
         name='api_register'),  # Add this line for registration

    path('admin/', admin.site.urls),
]

# Swagger UI -API Documentation-
schema_view = get_schema_view(
    openapi.Info(
        title="KitboxHealth API",
        default_version='v1',
        description="KitboxHealth API.",
        terms_of_service="https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/",
        contact=openapi.Contact(email="sanchezyander@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)

urlpatterns += [
    path('api/v1/docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]
