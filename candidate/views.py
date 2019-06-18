from django.shortcuts import render
from . import models
from student.models import Profile

# Create your views here.

def candidate_hp(request):
    details = Profile.objects.get(student_no=request.user)
    return render(request, 'candidate/intro.html', {'details':details})

def contestants(request):
    obj = models.Contestants.objects.all()
    length = len(obj)
    details = Profile.objects.get(student_no=request.user)
    return render(request, 'candidate/contestants.html', {'details':details, 'contestants':obj, 'length':length})
def currentCabinet(request):
    obj = models.CurrentCabinet.objects.all()
    length = len(obj)
    details = Profile.objects.get(student_no=request.user)
    return render(request, 'candidate/current.html', {'details':details, 'currentCabinets':obj, 'length':length})
def previousCabinet(request):
    obj = models.PreviousCabinet.objects.all()
    length = len(obj)
    details = Profile.objects.get(student_no=request.user)
    return render(request, 'candidate/previous.html', {'details':details, 'previousCabinets':obj, 'length':length})
