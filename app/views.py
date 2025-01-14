from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .serializers import BootcampRegistrationSerializer
from .models import BootcampRegistration

class BootcampRegistrationView(APIView):
    def post(self, request):
        serializer = BootcampRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Save to database
            registration = serializer.save()

            # Send email to user
            user_subject = "Bootcamp Registration Confirmation"
            user_message = f"Hi {registration.first_name},\n\nYou have successfully registered for the {registration.bootcamp_name} bootcamp."
            send_mail(
                user_subject,
                user_message,
                settings.EMAIL_HOST_USER,
                [registration.email],
                fail_silently=False,
            )

            # Send email to admin
            admin_subject = f"New Registration for {registration.bootcamp_name}"
            admin_message = (
                f"A new user has registered for the bootcamp:\n\n"
                f"Name: {registration.first_name} {registration.last_name}\n"
                f"Email: {registration.email}\n"
                f"Bootcamp: {registration.bootcamp_name}\n"
            )
            send_mail(
                admin_subject,
                admin_message,
                settings.EMAIL_HOST_USER,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            return Response({"message": "Registration successful!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
