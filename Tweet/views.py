from django.shortcuts import render
from .models import Tweet 
from .forms import TweetForm 
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
def index (request):
    return render(request , 'index.html') 

def Tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request, 'Tweet_list.html' ,{'tweets':tweets}) 

def Tweet_create(request):
    if request.method=='POST':
       form = TweetForm(request.POST, request.FILES)
       if form.is_valid():
           tweet =form.save(commit=False)
           tweet.user = request.user
           tweet.save()
           return redirect('tweet_list')
    else:
        form=TweetForm()
    return render(request, 'tweet_form.html', {'form':form})    

def Edit_tweet(request, tweet_id):
    tweet=get_object_or_404(Tweet , pk=tweet_id, user=request.user) # here user is used , a signed in user can only edit tweet .
    if request.method == 'POST' :
       form = TweetForm(request.POST, request.FILES , instance=tweet) 
       if form.is_valid():
           tweet =form.save(commit=False)
           tweet.user = request.user
           tweet.save()
           return redirect('tweet_list')
       else:
           form=TweetForm(instance=tweet)
       return render(request, 'tweet_form.html', {'form': form})     

def Delete_tweet(request, tweet_id):
    tweet= get_object_or_404(Tweet, pk=tweet_id, user=request.user) # user is used , only signin user can delete or edit of it's tweet
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})