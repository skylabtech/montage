
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
#from .forms import ContactForm


def home(request):
    # Your view logic here
    return render(request, 'appmontage/home.html')


def services(request):
    return render(request, 'appmontage/services.html')


def about_us(request):
    return render(request, 'appmontage/about_us.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        budget = request.POST.get('budget')

        # Construct the email message, including sender's email address
        email_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}\nBudget: {budget}\nSender's Email: {email}"

        # Send email, using sender's email as 'from_email'
        send_mail(
            'Contact Form Submission',
            email_message,
            email,  # Using sender's email as the 'from_email'
            ['origin21es@gmail.com'],  # Replace with recipient's email address
            fail_silently=False,
        )
        return HttpResponseRedirect(reverse('success'))
    else:
        return render(request, 'appmontage/contact_us.html')


def success(request):
    return render(request, 'appmontage/success.html')

























def landing(request):
    return render(request, 'appmontage/landing.html')