from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone


# Create your views here.
def project_list_view(request) :
    now = timezone.now()
    posts = Post.objects.all().filter(status=1,published_date__lte=now)
    context_project = {'posts':posts}
    return render(request,'projects.html',context_project)

def project_detail_view(request,pid) :
    post = Post.objects.get(id=pid,status=1,published_date__lte=timezone.now())
    post.counted_views += 1
    post.save()
    posts = list(Post.objects.filter(status=1, published_date__lte=timezone.now()))
    current_index = posts.index(post)
    previous_post = None
    next_post = None
    if current_index > 0:
        previous_post = posts[current_index - 1]
    if current_index < len(posts) - 1:
        next_post = posts[current_index + 1]
    context_project2 = {'post':post,'previous_post': previous_post,'next_post': next_post}
    return render(request,'project.html',context_project2)
