from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

from core.auth.serializers.reset_request import PasswordResetRequestSerializer

class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'detail': 'No user with this email'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Generate a password reset token
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            
            # Send email with password reset link
            reset_link = f"http://localhost:8000/reset-password/{uid}/{token}/"
            subject = 'Password Reset Request'
            message = render_to_string('password_reset_email.html', {'reset_link': reset_link})
            send_mail(subject, message, 'from@example.com', [email])
            
            return Response({'detail': 'Password reset link sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)