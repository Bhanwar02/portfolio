from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
import resend
from django.conf import settings


def home(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        try:
            # Save message in database
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )

            # Resend API key
            resend.api_key = settings.RESEND_API_KEY

            # Send email notification
            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": "kaurbhanwarpreet@gmail.com",
                "subject": f"New Portfolio Message from {name}",

                "html": f"""
                    <h2>New Portfolio Contact</h2>

                    <p><strong>Name:</strong> {name}</p>

                    <p><strong>Email:</strong> {email}</p>

                    <p><strong>Message:</strong></p>

                    <p>{message}</p>
                """
            })

            messages.success(request, "Message sent successfully!")

        except Exception as e:

            messages.error(request, f"EMAIL ERROR: {e}")

        return redirect("/")

    return render(request, "home.html")