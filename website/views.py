from django.shortcuts import render
from django.http import HttpResponse

def http_test(request) :
    return HttpResponse('Hello my frienddddd!')

def index_view(request) :
    return HttpResponse('Home page')

def about_view(request) :
    return HttpResponse('About page')

