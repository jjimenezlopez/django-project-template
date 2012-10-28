# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')


def do_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home.html')
            else:
                messages.error(request, _(u"Disabled account, please contact with an administrator."))
                return render(request, 'home.html')
        else:
            messages.error(request, _(u"Username or password is not valid."))
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def do_logout(request):
    logout(request)
    return render(request, 'home.html')
