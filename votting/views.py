from django.shortcuts import render
from student.models import Profile
from . import models
from django.http import HttpResponse

# Create your views here.

def votting_hp(request):
    details = Profile.objects.get(student_no=request.user)
    votes = models.Vote.objects.all()
    nominated = []
    non_nominated = []
    for i in votes:
        if i.nominated:
            nominated.append(i)
        else:
            non_nominated.append(i)
    context = {
        'l_nominated':len(nominated), 'l_nonNominated':len(non_nominated),
        'nominated':nominated, 'non_nominated':non_nominated, 'contestants':votes, 'details':details,
        'total_number':len(votes)
    }
    return render(request, 'votting/intro.html', context)

def nominated(request):
    details = Profile.objects.get(student_no=request.user)
    votes = models.Vote.objects.all()
    nominated = []
    for i in votes:
        if i.nominated:
            nominated.append(i)
    context = {
        'l_nominated': len(nominated),
        'nominateds': nominated, 'contestants': votes, 'details': details
    }
    return render(request, 'votting/nominated.html', context)

def nonNominated(request):
    details = Profile.objects.get(student_no=request.user)
    votes = models.Vote.objects.all()
    non_nominated = []
    for i in votes:
        if not i.nominated:
            non_nominated.append(i)
    context = {
        'l_nonNominated': len(non_nominated),
        'non_nominateds': non_nominated, 'contestants': votes, 'details': details
    }
    return render(request, 'votting/nonNominated.html', context)

def vote(request):
    details = Profile.objects.get(student_no=request.user)
    votes = models.Vote.objects.all()
    nominated = []
    non_nominated = []
    for i in votes:
        if i.nominated:
            nominated.append(i)
        else:
            non_nominated.append(i)
    context = {
        'l_nominated': len(nominated), 'l_nonNominated': len(non_nominated),
        'nominated': nominated, 'non_nominated': non_nominated, 'contestants': votes, 'details': details,
        'total_number': len(votes)
    }
    return render(request, 'votting/vote.html', context)
