import json

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from validate_email import validate_email


# Create your views here.
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data["email"]
        if not validate_email(email):
            return JsonResponse(
                {"email_error": "Email is invalid"},
                status=400,
            )
        if User.objects.filter(email=email).exists():
            return JsonResponse(
                {"email_error": "sory email in use, choose another one"},
                status=409,
            )
        return JsonResponse({"email_valid": True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data["username"]
        if not str(username).isalnum():
            return JsonResponse(
                {
                    "username_error": "username should only contain alphanumeric character"
                },
                status=400,
            )
        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {"username_error": "sory username in use, choose another one"},
                status=409,
            )
        return JsonResponse({"username_valid": True})


class RegistrationView(View):
    def get(self, request):
        return render(request, "authentication/register.html")

    def post(self, request):
        messages.success(request, "Seuccess whatsapp success")
        messages.warning(request, "Seuccess whatsapp warning")
        messages.info(request, "Seuccess whatsapp info")
        messages.error(request, "Seuccess whatsapp error")
        return render(request, "authentication/register.html")
