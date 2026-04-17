from django.shortcuts import render
from .models import Tour


# Create your views here.
def index(request):
    tours = Tour.objects.all()
    print(f"DEBUG: Found {tours.count()} tours in the database.")
    context = {
        'tours': tours
    }   
    return render(request, 'Tours/index.html', context)