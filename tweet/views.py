from django.shortcuts import render
from tweet.models import Tweet

# Create your views here.

def feed(request):
  userids = []
  for id in request.user.profile.related_to.all():
    userids.append(id)

  userids.append(request.user.id)
  tweets = Tweet.objects.filter(user_id__in=userids)[0:25]

  return render(request, 'feed.html', {'tweets': tweets})
