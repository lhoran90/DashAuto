from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def index(request):
    return HttpResponse("Welcome Home")

def home(request):
    return render(request,
                  'home/home.html',
                  {'section': 'home'})