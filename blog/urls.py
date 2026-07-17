from django.urls import path 
from blog.views import *
urlpatterns = [
    path('', project_list_view, name = 'index'),
    path('post-<int:pid>',project_detail_view, name = 'project'),
    path('category/<str:cat_title>',project_list_view,name='category'),
    path('tag/<str:tag_name>',project_list_view,name='tag'),
    path('search/',project_search,name='search'),
    
]