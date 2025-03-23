from django.urls import path
from .views import BlogListView

#urlspatterns
#the included URLconf '<module 'blog.urls' from '/home/nengkya/blog_project/blog/urls.py'>' does not appear to have any patterns in it
#if you see the 'urlpatterns' variable with valid patterns in the file then the issue is probably caused by a circular import
urlpatterns = [

    path('', BlogListView.as_view(), name = 'home')

]
