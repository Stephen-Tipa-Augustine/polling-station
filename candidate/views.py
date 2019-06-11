from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def candidate_hp(request):
    return render(request, 'candidate/intro.html')
