# reservation/views.py

from django.shortcuts import render, redirect
from .forms import UserForm, BookingForm
from .models import Train, Ticket
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        # Logic to authenticate user
        return redirect('home')
    return render(request, 'reservation/login.html')

def home(request):
    trains = Train.objects.all()
    form = BookingForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            form_data = form.save(commit=False)
            form_data.booked_user = request.user
            form_data.save()
            return redirect('booking_success')
        else:
            return redirect('login')  # Redirect to login if user is not authenticated
    context = {
        'trains': trains,
        'form': form
    }
    return render(request, 'reservation/home.html', context)

def dashboard(request):
    return render(request, 'reservation/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = UserForm()
    return render(request, 'reservation/register.html', {'form': form})

def registration_success(request):
    return render(request, 'reservation/registration_success.html')

@login_required
def booking_success(request):
    return render(request, 'reservation/booking_success.html')
