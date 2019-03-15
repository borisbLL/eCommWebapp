from django.http import HttpResponse
from django.shortcuts import render


from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
	context = { 
		"title":"Home Page", 
		"content":"Welcome to the homepage." 
	}
	return render(request, "home_page.html", context)

def about_page(request):
	context = { 
		"title":"About Page", 
		"content":"Welcome to the about page." 
	}
	return render(request, "about_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)		#instanciation of the class ContactForm
	context = { 
		"title":"Contact Page", 
		"content":"Welcome to the contact page.", 
		"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	return render(request, "contact/view.html", context)


def login_page(request):
	login_form = LoginForm(request.POST or None)		#instanciation of the class LoginForm
	print("Is user logged in ? : ")
	print(request.user.is_authenticated())
	if login_form.is_valid():
		print(login_form.cleaned_data)
	context = { 
		"form": login_form
	}

	return render(request, "auth/login.html", {})


def register_page(request):
	reg_form = RegisterForm(request.POST or None)		#instanciation of the class RegisterForm
	
	if reg_form.is_valid():
		print(reg_form.cleaned_data)

	return render(request, "auth/register.html", {})




