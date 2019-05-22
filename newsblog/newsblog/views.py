"Create a function to fire views"
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')
def about(request):
        return render(request,'about.html')
def aboutme(request):
    return render(request,'aboutme.html')
def portfolio(request):
    return  render(request,'portfolio.html')
def news(request):
    return render(request,'news.html')
def contact(request):
    return  render(request,'contact.html')
   
