# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
#from __future__ import unicode_literals

from django.shortcuts import render
# from django.conf import resources
# from .models import resources

# Create your views here.
def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)

def resources(request):
    context = {}
    template = 'resources.html'
    return render(request, template, context)

def resources2(request):
    context = {}
    template = 'resources2.html'
    return render(request, template, context)

def staff(request):
    context = {}
    template = 'staff.html'
    return render(request, template, context)

def daniel_onah(request):
    context = {}
    template = 'daniel_onah.html'
    return render(request, template, context)

def regina_reynolds(request):
    context = {}
    template = 'regina_reynolds.html'
    return render(request, template, context)

def david_zhang(request):
    context = {}
    template = 'david_zhang.html'
    return render(request, template, context)


def juan_botia(request):
    context = {}
    template = 'juan_botia.html'
    return render(request, template, context)

def news(request):
    context = {}
    template = 'news.html'
    return render(request, template, context)

def careers(request):
    context = {}
    template = 'careers.html'
    return render(request, template, context)

def daniel_biography(request):
    context = {}
    template = 'daniel_biography.html'
    return render(request, template, context)

def daniel_publications(request):
    context = {}
    template = 'daniel_publications.html'
    return render(request, template, context)



@login_required
def userProfile(request):
    user= request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request, template, context)