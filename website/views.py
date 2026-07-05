from django.shortcuts import render
from django.http import HttpResponse
from website.models import Post
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

def projects_view(request) :
    now = timezone.now()
    posts = Post.objects.all().filter(status=1,published_date__lte=now)
    context_project = {'posts':posts}
    return render(request,'projects.html',context_project)

def contact_view(request) :
    return render(request,'contact.html')

def project_view(request,pid) :
    post = Post.objects.get(id=pid,status=1)
    post.counted_views += 1
    post.save()
    context_project2 = {'post':post}
    return render(request,'project.html',context_project2)


