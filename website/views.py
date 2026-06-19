from django.shortcuts import render
from django.http import HttpResponse

def index_view(request) :
    context = {'name':'Sina','lastname':'Sabetimani'}
    return render(request,'index.html',context)

def education_view(request) :
    return render(request,'education.html')

def skills_view(request) :
    return render(request,'skills.html')

def languages_view(request) :
    return render(request,'languages.html')

def projects_view(request) :
    context2 = {'title':'AI THESIS IN TYPE 2 DIABETES DIAGNOSIS','info':'Prediction of Type 2 Diabetes Based on Anthropometric Indices Using Machine Learning Algorithms in Mashhad Persian Cohort Population.'}
    return render(request,'projects.html',context2)

def contact_view(request) :
    return render(request,'contact.html')



