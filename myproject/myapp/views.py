from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Compose Email
            subject = f"New Contact Form Submission from {name}"
            full_message = f"Message from {name} ({email}):\n\n{message}"

            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['dangerm249@gmail.com'],  # Replace with your email
            )
            return render(request, 'perplex.html')  # Redirect to thank you page
    return render(request, 'index.html', {'form': form})