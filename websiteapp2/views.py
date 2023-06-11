from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
	# below grabs everything on the table and assigns it to the variable records
	records_ = Record.objects.all()


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
		return render(request, 'home.html', {'records':records_})



def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out...")
	return redirect('home_')


def register_user(request):
	if request.method == 'POST':
		# If post, then our form will be turned into SignUpForm
		form = SignUpForm(request.POST)
		# below checks if the form is valid
		if form.is_valid():
			# below if form is valid, form.save()
			form.save()
			# Authenticate and Login ; cleaned data from request.POST
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# below authenticate user
			user = authenticate(username=username, password=password)
			# below if user is authenticated, then login the user because he is requesting
			login(request, user)
			# if successful, print out messages below
			messages.success(request, "Registered Properly")
			return redirect('home_')
	else: # below no more request.POST because user is just looking and not filling any textboxes/form
		form_ = SignUpForm()
		return render(request, 'register.html', {'form':form_}) # form_ from 1 line above this

	return render(request, 'register.html', {'form':form_}) # form_ from 3 lines above this


def customer_record(request, pk):
	# if the user is authenticated, perform below
	if request.user.is_authenticated:
		# Look up Records. id below is from migration fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record}) # customer_record from 1 line above this
	else:
		# if the user is not authenticated, perform below
		messages.success(request, "Have to be logged in to view that Page")
		return redirect('home_')


# deleting records is the same as logging out
def delete_record(request, pk):
	if request.user.is_authenticated:
		# if logged in and authenticated, perform below
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Successfully Deleted the Record(s)")
		return redirect('home_')
	else:
		#if not logged in, perform below
		messages.success(request, "Must Login First before you can delete Record(s)")
		return redirect('delete_record_')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added")
				return redirect('home_')
		return render(request, 'add_record.html', {'form':form}) # customer_record from 1 line above this
	else:
		messages.success(request, "You must be Logged In")
		return redirect('home_')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		# instance=curent_record is to get records from the database
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Now Updated")
			return redirect('home_')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You must be logged in")
		return redirect('home_')

