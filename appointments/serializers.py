from rest_framework import serializers

from core.models import User

from .models import Appointment, Doctor, Patient


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        extra_kwargs = {
            'patient': {'read_only': True}
        }


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    gender = serializers.CharField(required=True)
    marital_status = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=True)
    address = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    zip_code = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    primary_language = serializers.CharField(required=True)
    referred_by_physician = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = (
            'username', 'password', 'first_name', 'last_name', 'email',
            'gender', 'marital_status', 'date_of_birth', 'address',
            'city', 'state', 'zip_code', 'phone', 'primary_language',
            'referred_by_physician'
        )

    def create(self, validated_data):
        patient_data = {
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            'gender': validated_data.pop('gender'),
            'marital_status': validated_data.pop('marital_status'),
            'date_of_birth': validated_data.pop('date_of_birth'),
            'address': validated_data.pop('address'),
            'city': validated_data.pop('city'),
            'state': validated_data.pop('state'),
            'zip_code': validated_data.pop('zip_code'),
            'phone': validated_data.pop('phone'),
            'primary_language': validated_data.pop('primary_language'),
            'referred_by_physician': validated_data.pop('referred_by_physician', False),
        }

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )

        Patient.objects.create(user=user, **patient_data)

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'patient']

    def get_patient(self, obj):
        try:
            return str(obj.patient.id)
        except Patient.DoesNotExist:
            return None
