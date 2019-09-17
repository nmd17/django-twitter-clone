"""twitterClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from tweet.views import feed
from .views import homepage, profile, signout, follow, stopfollow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('feed/', feed, name='feed'),
    path('signout/', signout.as_view(), name='signout'),
    path('<str:username>/', profile.as_view(), name='profile'),
    path('<str:username>/follow/', follow.as_view(), name='follow'),
    path('<str:username>/stopfollow/', stopfollow.as_view(), name='stopfollow'),
    
]
