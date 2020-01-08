from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'my_site/index.html')

def projects(request):
    return render(request, 'my_site/projects.html')

def contactme(request):
    return render(request, 'my_site/contactme.html')

def aboutme(request):
    return render(request, 'my_site/aboutme.html')
