from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from requests import auth


def UserLoginPagecall(request):
    return render(request, 'userapp/UserLoginPage.html')

# Logic for login
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

def UserLoginLogic(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect based on the length of the username
            if len(username) == 10:
                return redirect('adminapp:AdminHomePage')  # Redirect to adminapp for 10-digit username
            elif len(username) == 4:
                return redirect('userapp:NewUserPage')  # Redirect to userapp for 4-digit username
            else:
                messages.error(request, "Invalid username length")
                return redirect('userapp:UserLoginLogic')  # Stay on the login page for invalid length
        else:
            messages.error(request, "Invalid username or password")
            return redirect('userapp:UserLoginLogic')  # Stay on login page if credentials are wrong

    return render(request, 'userapp/UserLoginPage.html')

def UserLogout(request):
    logout(request)  # Logs out the user
    messages.success(request, "You have been logged out successfully.")  # Optional: Add a success message
    return redirect('eventapp:ProjectHomePage')  # Redirect to homepage after logout

def NewUserPage(request):
    return render(request, 'userapp/newuserpage.html')
from django.shortcuts import render, redirect
from .forms import EventForm  # Make sure to create an EventForm

# userapp/views.py

from django.shortcuts import render, redirect
from .forms import EventForm  # Import the EventForm
from .models import Event  # Import the Event model

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()  # Save the event to the database
            return redirect('userapp:event_list')  # Redirect to the event list after saving
    else:
        form = EventForm()  # Create an empty form
    return render(request, 'userapp/add_event.html', {'form': form})

def event_list(request):
    events = Event.objects.all()  # Get all events from the database
    return render(request, 'userapp/event_list.html', {'events': events})

