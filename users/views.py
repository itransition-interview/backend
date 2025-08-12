from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny


class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        phone = request.data.get("phone")
        password = request.data.get("password")

        if not phone or not password:
            return Response({"error": "Phone and password are required."}, status=400)

        if User.objects.filter(phone=phone).exists():
            return Response({"error": "Phone already exists."}, status=400)

        User.objects.create_user(username=username, phone=phone, password=password)
        return Response({"message": "User created successfully."}, status=201)


class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone = request.data.get("phone")
        password = request.data.get("password")

        user = authenticate(phone=phone, password=password)
        print("USER", user)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "id": user.id,
                    "role": user.role,
                }
            }, status=200)
        else:
            return Response({"error": "Invalid credentials."}, status=401)
