from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
	return render(request, 'register.html', {})