from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

#create your views here
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
