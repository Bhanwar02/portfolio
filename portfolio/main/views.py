from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail

def home(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

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

            from_email='kaurbhanwarpreet@gmail.com',

            recipient_list=['kaurbhanwarpreet@gmail.com'],

            fail_silently=False,
        )

        return redirect('/')

    return render(request, 'home.html')