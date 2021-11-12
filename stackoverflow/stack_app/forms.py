from django import forms
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter display name','class':'form-control shadow border-dark'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter email address','class':'form-control shadow border-dark'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter ur password','class':'form-control shadow border-dark'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter the password again','class':'form-control shadow border-dark'}))