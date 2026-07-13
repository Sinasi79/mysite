from django.urls import path 
from blog.views import *
urlpatterns = [
    path('', project_list_view, name = 'index'),
    path('post-<int:pid>',project_detail_view, name = 'project'),
    
]