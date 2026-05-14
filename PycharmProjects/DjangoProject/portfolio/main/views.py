from django.shortcuts import render, redirect

from portfolio import settings
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

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
                recipient_list=['kaurbhanwarpreet@gmail.com'],
                fail_silently=True,
            )


            return redirect('/')


        except Exception as e:
            print("ERROR:", e)
            messages.error(request, "Failed to send message.")
            return redirect('/')
    messages.success(request, "Message sent successfully!")
    return render(request, 'home.html')