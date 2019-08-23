from django.shortcuts import render
import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def home(request):
    if request.POST:
        keyword = request.POST['keyword']

        t=[]

        for tweet_info in tweepy.Cursor(api.search, q=keyword, count=100, tweet_mode='extended').items(100):
            if 'retweeted_status' in dir(tweet_info):
                tweet=tweet_info.retweeted_status
            else:
                tweet=tweet_info
            polarity = TextBlob(tweet.full_text).sentiment.polarity
            subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
            t.append({"text":tweet.full_text,"link":tweet.id,"screen_name":tweet.user.screen_name,"polarity":polarity,"subjectivity":subjectivity})
        context = {
            'res':t
        }
        return render(request, 'herald/main.html', context)
    else:
        return render(request, 'herald/main.html')