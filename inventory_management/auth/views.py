from django.shortcuts import redirect, render, ridirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .contrib.auth.models import User

#import the registerform from forms .py
from .forms import RegisterForm


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_messsage = 'invalid credentials'
    return render(request, 'account/login.html', {'error_message': error_messsage})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('home')
    
    #usung the decorator function
@login_required
def home_view(request):
    return render(request, 'home/home.html')


    #protected view 

class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'

    #next to redirect to after url 
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/  protected.html')


