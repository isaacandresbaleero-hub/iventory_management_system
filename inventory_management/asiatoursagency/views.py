from django.shortcuts import render, redirect
from .models import Tour, Tourform 


# Create your views here.
def index(request):
    tours = Tour.objects.all()
    print(f"DEBUG: Found {tours.count()} tours in the database.")
    context = {
        'tours': tours
    }   
    return render(request, 'Tours/index.html', context)

def contact(request):
    if request.method == 'POST':
        form = Tourform(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('index')
    else:
        form = Tourform()
    return render(request, 'Tours/contact.html', {'form': form})okk