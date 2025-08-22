def about_view(request):
	return render(request, 'about.html')
def therapy_view(request):
	return render(request, 'therapy.html')
def meditation_view(request):
	return render(request, 'meditation.html')
def contact_view(request):
	return render(request, 'contact.html')
from .forms import ApproachForm
from .models import Approach
def approach_form_view(request):
	from django.contrib import messages
	from django.shortcuts import redirect
	if not request.user.is_authenticated:
		messages.error(request, 'You must be logged in to submit the form.')
		return redirect('login')
	if request.method == 'POST':
		form = ApproachForm(request.POST)
		if form.is_valid():
			approach = form.save(commit=False)
			approach.user = request.user
			approach.save()
			messages.success(request, 'Your approach has been submitted successfully!')
			return redirect('approach_success')
		else:
			messages.error(request, 'Please correct the errors below.')
	else:
		form = ApproachForm()
	return render(request, 'approach_form.html', {'form': form})
def approach_success_view(request):
	return render(request, 'approach_success.html')

def payment_details_view(request):
	from django.shortcuts import redirect
	# If the form posts (confirm payment), redirect to success page
	if request.method == 'POST':
		return redirect('payment_success')
	return render(request, 'payment_details.html')
def payment_success_view(request):
	return render(request, 'payment_success.html')
from django.contrib.auth import logout

def logout_view(request):
	logout(request)
	from django.contrib import messages
	messages.success(request, 'You have been logged out.')
	return redirect('login')
def home_view(request):
	return render(request, 'home.html')
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def register_view(request):
	from django.contrib import messages
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Registration successful! Please log in.')
			return redirect('login')
		else:
			messages.error(request, 'Please correct the errors below.')
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('home')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})
from django.shortcuts import render

# Create your views here.
