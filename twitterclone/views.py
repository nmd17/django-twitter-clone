from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from twitteruser.models import Profile
from tweet.forms import TweetForm
from tweet.models import Tweet
from notification.models import Notification
from django.views import View

def homepage(request):
    if request.user.is_authenticated:
        return redirect('/' + request.user.username + '/')
    else:
        if request.method == 'POST':
            if 'signupform' in request.POST:
                signupform = SignUpForm(data=request.POST)
                if signupform.is_valid():
                    data = signupform.cleaned_data
                    user = User.objects.create_user(username=data['username'], password=data['password'])
                    user.profile.bio = data['bio']
                    user.profile.birth_date = data['birth_date']
                    login(request, user)
                    return redirect('/')
            else:
                signinform = SignInForm(data=request.POST)
                signupform = SignUpForm()
        
                if signinform.is_valid():
                    login(request, signinform.get_user())
                    return redirect('/')
        else:
            signupform = SignUpForm()
            signinform = SignInForm()
  
    return render(request, 'homepage.html', {'signupform': signupform, 'signinform': signinform})



class profile(View):
    form_class = TweetForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'profile.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST)

        if form.is_valid():
                
                data = form.cleaned_data
                user = request.user
                tweet = Tweet.objects.create(body=data['body'])
                user.profile.tweets.add(tweet)
                
                redirecturl = request.POST.get('redirect', '/')

                return redirect(redirecturl)

class signout(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class follow(View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        message = request.user.profile
        notification = Notification.objects.create(sender=request.user.profile,
                                               recipient=user.profile,
                                               message=message)

        user.profile.followers.add(request.user.profile)
        user.profile.recipient_notification.add(notification)

        return redirect('/' + user.username + '/')


class stopfollow(View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        user.profile.followers.remove(request.user.profile)

        return redirect('/' + user.username + '/')


