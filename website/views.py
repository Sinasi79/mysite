from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def index_view(request) :
    context = {'name':'Sina','lastname':'Sabetimani'}
    return render(request,'index.html',context)

def education_view(request) :
    return render(request,'education.html')

def skills_view(request) :
    return render(request,'skills.html')

def languages_view(request) :
    return render(request,'languages.html')

def contact_view(request) :
    return render(request,'contact.html')



