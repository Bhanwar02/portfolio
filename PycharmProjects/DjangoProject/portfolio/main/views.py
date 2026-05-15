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

        try:
            # Save to database
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )

            # Send email
            send_mail(
                subject=f"New Portfolio Message from {name}",

                message=f"""
Name: {name}
Email: {email}

Message:
{message}
                """,

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=["kaurbhanwarpreet@gmail.com"],

                fail_silently=False,
            )

            messages.success(request, "Message sent successfully!")

        except Exception as e:

            print("EMAIL ERROR:", e)

            messages.warning(
                request,
                "Message saved successfully, but email notification failed."
            )

        return redirect("/")

    return render(request, "home.html")