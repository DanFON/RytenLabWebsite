# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

# Create your views here.

def contact_us(request):
    title = 'Contact us.'
    form = contactForm(request.POST or None)
    confirm_message= None
    #context = {'title' : title, 'form': form,}

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['message']
        subject = 'Message from BRAINEACV2'
        message ='%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo =[settings.EMAIL_HOST_USER]
        send_mail(subject,message, emailFrom,emailTo, fail_silently=True)
        title= "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you."
        form  = None

    context = {'title' : title,'form': form, 'confirm_message': confirm_message,}
   # context = locals()
    template = 'contact_us.html'
    return render(request, template, context)