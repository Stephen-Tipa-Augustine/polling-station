from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def votting_hp(request):
    return render(request, 'votting/intro.html')
