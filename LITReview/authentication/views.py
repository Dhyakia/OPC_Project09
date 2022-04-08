from django import forms
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from . import forms


def login(request):

    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    if request.method == 'GET':
        form = form_class()
        message = ''
        return render(request, template_name, context={'form': form, 'message': message})

    elif request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                auth_login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)

        message = 'Identifiants invalides.'
        return render(request, template_name, context={'form': form, 'message': message})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')


def signup(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'authentication/signup.html', context={'form': form})
