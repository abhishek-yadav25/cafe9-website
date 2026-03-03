from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    return render(request, 'main/index.html')

def menu(request):
    return render(request, 'main/menu.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    return render(request, 'main/contact.html')


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = "Thank You for Contacting Cafee⁹'"
        msg = f"""
Hello {name},

Thank you for contacting Cafee⁹'.

We appreciate you reaching out to us.
Our team will get back to you soon.

Regards,
Cafee⁹' Team
"""

        send_mail(
            subject,
            msg,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        # ✅ success message AFTER form submit
        messages.success(
            request,
            "Your details have been sent successfully!"
        )

    return render(request, "main/contact.html")