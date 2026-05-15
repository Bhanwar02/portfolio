from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def home(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save in database

        try:
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            send_mail(
                subject=f"New Portfolio Message from {name}",

                message=f"""
Name: {name}
Email: {email}

Message:
{message}
                """,

                from_email="kaurbhanwarpreet@gmail.com",

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