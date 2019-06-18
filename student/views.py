from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json

# Create your views here.
@login_required(login_url='start')
def posts(request):
    l = models.Posts.objects.order_by('time')
    comments = models.PostComments.objects.order_by('time')
    likes = models.PostLikes.objects.order_by('time')
    details = models.Profile.objects.get(student_no=request.user)
    o = len(likes)
    n = len(l)
    m = len(comments)
    post = []
    comment = []
    like = []
    for i in range(n-1, -1, -1):
        post.append(l[i])
    for i in range(m-1, -1, -1):
        comment.append(comments[i])
    for i in range(o-1, -1, -1):
        like.append(l[i])
    return render(request, 'student/posts.html', {'details':details, 'posts':post, 'comments':comment, 'likes':like})
@login_required(login_url='start')
def feedback(request):
    comments = models.Comment.objects.all()
    details = models.Profile.objects.get(student_no=request.user)
    return render(request, 'student/feedback.html', {'comments':comments, 'details':details})
@login_required(login_url='start')
def profile(request):
    details = models.Profile.objects.get(student_no=request.user)
    return render(request, 'student/profile.html', {'details':details})
def start_page(request):
    return render(request, 'polling_station/start_page.html')
@login_required(login_url='start')
def home_page(request):
    details = models.Profile.objects.get(student_no=request.user)
    return render(request, 'polling_station/intro.html', {'details':details})
def enrolled(request):
    return render(request, 'student/enrolled.html')
def comment(request):
    form = forms.CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    return redirect(request.META.get('HTTP_REFERER'))

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, "student/login.html", {'form':form})
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user = post.save()
            login(request, user)
            user_detail = models.Profile
            user_detail.student_no = request.user
            user_detail.save()
            return redirect('student:enrolled')
    else:
        form = UserCreationForm()
    return render(request, 'student/enroll1.html', {'user_form':form})

def enroll_page(request):
    if request.method == 'POST':
        form = forms.StudentDetails(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('student:enroll1')
    else:
        form = forms.StudentDetails()
    return render(request, "student/enroll.html", {'form':form})

def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return render(request, 'student/logout.html')

def make_post(request):
    if request.method == 'POST':
        form = forms.Post(request.POST, request.FILES)
        details = models.Profile.objects.get(student_no=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.userPhoto = details.photo
            new = post.post[:20].split(' ')
            new = '_'.join(new) + '_'
            for i in "./,\n":
                new = new.replace(i, '')
            post.key = new + str(request.user)
            post.keyComment = post.key + '_1'
            post.save()
    return redirect(request.META.get('HTTP_REFERER'))

def post_comment(request, slug):
    if request.method == 'POST':
        form = forms.PostComment(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.post = str(slug)
            post.save()
            comment = models.Posts.objects.all()
            for i in comment:
                if i.post == str(slug):
                    i.comments +=1
                    i.save()
    return redirect(request.META.get('HTTP_REFERER'))

def like_post(request, slug):
    fuck = models.Posts.objects.all()
    obj = models.PostLikes.objects.all()
    n = len(obj)
    for i in obj:
        print(i.likes)
        if i.post == str(slug):
            if (i.user == request.user) and i.likes == True:
                for j in fuck:
                    if j.post == str(slug):
                        j.likes -= 1
                        j.save()
                        i.likes = False
                        i.save()
                        break
            elif (i.user == request.user) and i.likes == False:
                for j in fuck:
                    if j.post == str(slug):
                        j.likes += 1
                        j.save()
                        i.likes = True
                        i.save()
                        break
        elif i == obj[n-1] and i.post != str(slug):
            like = models.PostLikes()
            like.post = str(slug)
            like.likes = True
            like.user = request.user
            like.save()
            for j in fuck:
                if j.post == str(slug):
                    j.likes += 1
                    j.save()
    if len(obj) == 0:
        like = models.PostLikes()
        like.post = str(slug)
        like.likes = True
        like.user = request.user
        like.save()
        for j in fuck:
            if j.post == str(slug):
                j.likes += 1
                j.save()
    return redirect(request.META.get('HTTP_REFERER'))
