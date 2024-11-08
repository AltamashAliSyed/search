
from django.urls import path
from .views import post,search
urlpatterns = [
   path('',post,name='post'),
   path('search/',search,name='search'),
]