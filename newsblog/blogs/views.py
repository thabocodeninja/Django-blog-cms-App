from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse

# Create your views here.
def blog(request):
    blogs = Blog.objects.all().order_by('date')
    return render(request,'blogs/blog.html',{'blog':blogs})

def blog_detail(request,slug):
   # return HttpResponse(slug)
   blog = Blog.objects.get(slug=slug)
   return render(request,'blogs/blog_detail.html',{'blog':blog})