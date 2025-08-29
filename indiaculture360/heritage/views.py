from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import HeritageSite
from .forms import ContactForm
import json


# Profile Page (used as home in urls.py)
def profile_view(request):
    query = request.GET.get('search')
    sites = HeritageSite.objects.filter(name__icontains=query) if query else HeritageSite.objects.all()
    site_data = list(sites.values())
    return render(request, 'profile.html', {
        'sites': sites,
        'site_data_json': json.dumps(site_data)
    })

# Explore Page
def explore(request):
    query = request.GET.get('search')
    sites = HeritageSite.objects.filter(name__icontains=query) if query else HeritageSite.objects.all()
    site_data = list(sites.values())
    return render(request, 'explore.html', {
        'sites': sites,
        'site_data_json': json.dumps(site_data)
    })


# Static Pages
def story(request):
    return render(request, 'story.html')

def about(request):
    return render(request, 'about.html')

def mission(request):
    return render(request, 'ourmission.html')


# Contact Page with Email Form
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                subject=cd['subject'],
                message=f"Message from {cd['name']} ({cd['email']}):\n\n{cd['message']}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[getattr(settings, 'CONTACT_EMAIL', settings.EMAIL_HOST_USER)],  
                fail_silently=False
            )
            return render(request, 'perplex.html')  # Success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


#Authentication
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Logged in successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('profile')
        else:
            messages.error(request, "Registration failed. Check the form.")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
