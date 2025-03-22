#from django.contrib.admin.site import register
#ModuleNotFoundError: No module named 'django.contrib.admin.site'
from django.contrib import admin
from .models import Post

#register your models here
admin.site.register(Post)
