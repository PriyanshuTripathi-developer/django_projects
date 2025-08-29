from django.shortcuts import render
from .models import Herb

def home(request):
    query = request.GET.get('search')
    if query:
        herbs = Herb.objects.filter(name__icontains=query)
    else:
        herbs = Herb.objects.all()
    return render(request, 'herbal_app/home.html', {'herbs': herbs})
