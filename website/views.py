from django.shortcuts import render
from django.http import HttpResponse

def index_view(request) :
    return render(request,'index.html')

def education_view(request) :
    return render(request,'education.html')

def skills_view(request) :
    return render(request,'skills.html')

def languages_view(request) :
    return render(request,'languages.html')

def projects_view(request) :
    return render(request,'projects.html')

def contact_view(request) :
    return render(request,'contact.html')


