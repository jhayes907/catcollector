from django.shortcuts import render
from django.http import HttpResponse

# Temp:  Create your classes here
class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
    def __str__(self):
        return f"{self.name}"

cats = [
    Cat('Rufus', 'tabby', 'crazy cat', 103),
    Cat('Nibbler', 'calico', 'hungry', 40),
    Cat('Jerry', 'tomcat', 'determined', 4),
]

# Create your views here.
def index(request):
    return render(request,'index.html', { 'cats': cats })

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

