from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return HttpResponse('<h1>welcome to django classes mr. punit singh vishen</h1>')
