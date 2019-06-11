"""polling_station URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views

app_name = 'student'

urlpatterns = [
    # re_path(r'^$', views.student_hp, name='homepage'),
    path('<str:slug>/login', views.login_page),
    path('login/', views.login_page, name='login'),
    path('start-enroll/', views.enroll_page, name='enroll'),
    path('profile/', views.profile, name='profile'),
    path('feedback/', views.feedback, name='feedback'),
    path('User-comment/', views.comment, name='comment'),
    path('posts/', views.posts, name='posts'),
    path('posts/let-me-create-a-post/', views.make_post, name='make_post'),
    path('posts/add-comment-to-current-post/<str:slug>', views.post_comment, name='post_comment'),
    path('posts/like-current-post/<str:slug>', views.like_post, name='like'),
    path('create-a-user-account/', views.create_user, name='enroll1'),
    path('enrolled-thanks/', views.enrolled, name='enrolled'),
    path('log-out-current-user/', views.logout_user, name='logout'),

]
