from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib import messages

from last.forms import EmailForm, RegisterUserForm
from django.conf import settings



def home(request):
    return render(request, 'last/index.html')


class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'last/susccessfull.html'

    def get(self, request):
        form = self.form_class()
        return render(request,'last/successfull.html',{'email_form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, 'last/successfull.html',
                              {'email_form': form, 'error_message': 'Электрондық пошта мекенжайына жіберілді %s' % email})
            except:
                return render(request, 'last/successfull.html',
                              {'email_form': form, 'error_message': 'Не тіркеме тым үлкен немесе бүлінген'})

        return render(request, 'last/successfull.html',
                      {'email_form': form, 'error_message': 'Электрондық поштаны жіберу мүмкін емес. Тағы жасауды сәл кейінірек көріңізді өтінеміз'})




class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'last/register.html'
    success_url = reverse_lazy('login')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("There is some problem .. Try again.."))
            return redirect('login')
    else:
        return render(request, 'last/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')

#
