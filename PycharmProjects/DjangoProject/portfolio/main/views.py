from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
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
        try:
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

            messages.success(request, "Message sent successfully!")

            return redirect('/')

        except Exception as e:
            print(e)
            messages.error(request, "Failed to send message.")
            return redirect('/')

    return render(request, 'home.html')