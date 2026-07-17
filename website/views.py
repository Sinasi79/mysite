from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from website.models import Contact
from website.forms import ContactForm
from django.contrib import messages

def index_view(request) :
    context = {'name':'Sina','lastname':'Sabetimani'}
    return render(request,'index.html',context)

def education_view(request) :
    return render(request,'education.html')

def skills_view(request) :
    return render(request,'skills.html')


def contact_view(request) :
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid() :
            ticket = form.save(commit=False)
            ticket.name = 'Anonymous'
            ticket.save()
            messages.add_message(request,messages.SUCCESS,'Your ticket has been submitted successfully.')
        else : 
            messages.add_message(request,messages.ERROR,'Your ticket was not submitted.')

    else:
        form = ContactForm()

    return render(request,'contact.html',{'form':form})



