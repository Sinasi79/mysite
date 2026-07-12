from django.urls import path 
from website.views import *

urlpatterns = [
    path('', index_view),
    path('education', education_view),
    path('skills', skills_view),
    path('languages', languages_view),
    path('contact', contact_view),
    
]