from django.urls import path 
from blog.views import *
urlpatterns = [
    path('', projects_view, name = 'index'),
    path('post-<int:pid>',project_view, name = 'project'),
    
]