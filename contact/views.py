from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """
    A view to render the contact form
    and send message
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send the email and redirect to a thank you page
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipient = settings.DEFAULT_FROM_EMAIL
            subject = f'BLS Digital contact form: {name}, {from_email}'
            send_mail(subject, message, from_email, [recipient])
            return redirect('thank_you')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def thank_you(request):
    """
    A view to render the thank you page
    """
    return render(request, 'contact/thank_you.html')
