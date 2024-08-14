from django.contrib import admin
from django.urls import include, path
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
