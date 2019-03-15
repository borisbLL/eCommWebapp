from django import forms

# django customizing form fields widgets

class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your full name"}))
	email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your Email"}))
	message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Message"}))

# adding custom validation

def clean_email(self):
	email = self.cleaned_email.get("email")
	if not "@" in email:
		raise forms.ValidationError("Error: email must be a valid format")
	return email


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
