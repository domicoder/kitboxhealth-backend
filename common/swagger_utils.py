from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from appointments.serializers import UserRegistrationSerializer

user_registration_schema = swagger_auto_schema(
    request_body=UserRegistrationSerializer,
    responses={
        201: openapi.Response(
            description="User registered successfully.",
            examples={
                "application/json": {
                    "user": {
                        "username": "johndoe",
                        "first_name": "John",
                        "last_name": "Doe",
                        "email": "johndoe@example.com",
                        "patient": {
                            "id": "16b903bb-9560-47f2-a974-e8c1bc68d697",
                            "last_edited": "2024-08-14T11:59:38.073486Z",
                            "first_name": "Victor",
                            "last_name": "Doe",
                            "gender": "Male",
                            "marital_status": "Single",
                            "date_of_birth": "1990-01-01",
                            "address": "123 Main St",
                            "city": "Somewhere",
                            "state": "NY",
                            "zip_code": "12345",
                            "phone": "555-1234",
                            "primary_language": "English",
                            "referred_by_physician": "false",
                            "created": "2024-08-14T11:59:38.073409Z",
                            "user": "4c98bcf4-55a0-46ac-ad5d-639f0cdad383"
                        }
                    },
                    "token": "5361c44axxxxc4049076cxxxx8fdfacaf2ee9708",
                    "detail": "User registered successfully."
                }
            }
        ),
        400: "Bad Request"
    }
)

custom_auth_token_schema = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
        }
    ),
    responses={
        200: openapi.Response(
            description="Token and user details",
            examples={
                "application/json": {
                    "token": "123abc456def",
                    "user": {
                        "id": "52a31439-e68a-47ee-8d00-882d5b1a6d5d",
                        "username": "johndoe",
                        "first_name": "John",
                        "last_name": "Doe",
                        "email": "johndoe@example.com",
                        "patient": "58be6cd8-8b93-4585-a681-5d931899c452"
                    }
                }
            }
        ),
        400: "Invalid Credentials"
    }
)
