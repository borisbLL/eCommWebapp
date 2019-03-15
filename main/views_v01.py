from django.http import HttpResponse
from django.shortcuts import render

# def home_page(request):
#	return HttpResponse("<h1>Hello world</h1>")

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
	context = { 
		"title":"Contact Page", 
		"content":"Welcome to the contact page." 
	}
	if request.method == "POST":
		# print(request.POST)
		print(request.POST.get('fullname'))
		print(request.POST.get('email'))
		print(request.POST.get('message'))
	return render(request, "contact/view.html", context)