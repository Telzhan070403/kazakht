from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(label='Пайдаланушы аты')
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Пайдаланушы аты', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(required=True, label='Электрондық пошта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Құпия сөз', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Құпия сөзді қайталаңыз', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Есімі', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Тегі', widget=forms.TextInput(attrs={'class': 'form-input'}))
    city = forms.CharField(label='Қала', widget=forms.TextInput(attrs={'class': 'form-input'}))
    address = forms.CharField(label='Мекенжай', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'city', 'address')

