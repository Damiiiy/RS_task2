from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .serializers import BootcampRegistrationSerializer
from .models import BootcampRegistration


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.timezone import now
from django.conf import settings
from .serializers import BootcampRegistrationSerializer


@api_view(['POST'])
def register_bootcamp(request):
    serializer = BootcampRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        # Save to database
        registration = serializer.save()
        print(registration)

        # Render the HTML email template
        html_content = render_to_string('email/email_template.html', {
            'full_name': registration.full_name,
            'role': registration.role,
            'year': now().year,
        })

        # Send email to user
        subject = "Bootcamp Registration Confirmation"
        email = EmailMultiAlternatives(
            subject,
            None,
            settings.EMAIL_HOST_USER,
            [registration.email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()

        # Send email to admin
        admin_subject = f"New Registration for {registration.role}"
        admin_message = (
            f"A new user has registered for the bootcamp:\n\n"
            f"Name: {registration.full_name}\n"
            f"Email: {registration.email}\n"
            f"Role: {registration.role}\n"
        )
        EmailMultiAlternatives(
            admin_subject,
            admin_message,
            settings.EMAIL_HOST_USER,
            [settings.ADMIN_EMAIL],
        ).send()

        return Response({"message": "Registration successful!"}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)