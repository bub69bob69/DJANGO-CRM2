from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
	# check to see if logging in
	if request.method == 'POST':
		#do something
		# below taken from <input type="text" class="form-control" name="username",
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You are Logged in")
			return redirect('home_')
		else:
			messages.success(request, "An Error has occurred, please try again")
			return redirect('home_')
	else:
		return render(request, 'home.html', {})



def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out...")
	return redirect('home_')


def register_user(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and Login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			# if successful, print out messages below
			messages.success(request, "registered properly")
			return redirect('home')
	else: # below no more request.POST because user is just looking and not filling any textboxes/form
		form = SignupForm()
		return render(request, 'register.html', {'form':form})