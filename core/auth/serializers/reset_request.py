from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()