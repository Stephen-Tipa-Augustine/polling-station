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

app_name = 'votting'
urlpatterns = [
    re_path(r'^$', views.votting_hp, name='homepage'),
    path('nominated-candidates/', views.nominated, name='nominated'),
    path('non-nominated-candidates/', views.nonNominated, name='non-nominated'),
    path('vote-your-favourites-candidates/', views.vote, name='vote'),
]
