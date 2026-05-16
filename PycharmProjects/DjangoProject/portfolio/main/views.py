from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Validation
        if not name or not email or not message:
            messages.error(request, "Please fill all required fields.")
            return redirect("/")

        try:
            # Save message in database
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )

            # Send email notification
            send_mail(
                subject=f"New Portfolio Message from {name}",

                message=f"""
New portfolio contact message

Name: {name}
Email: {email}

Message:
{message}
                """,

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=["kaurbhanwarpreet@gmail.com"],

                fail_silently=True,
            )

            messages.success(
                request,
                "Message sent successfully!"
            )

        except Exception:

            messages.error(
                request,
                "Something went wrong. Please try again later."
            )

        return redirect("/")

    return render(request, "home.html")