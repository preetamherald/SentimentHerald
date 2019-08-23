from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob

#twitter authentication
#You can find your key and token @ developer.twitter.com/en/apps
consumer_key = 'OaIsCNwEYwRo3Yt85lThc72Sb'
consumer_secret = 'oIZdYrslSbLtoQt3lrSIompVXY7SScmz7pzLXxPNwPDRlTrRXQ'

access_token = '871926186317893635-iV0lB9eEKv5AyCz0PXzRqqfBil1c0U1'
access_token_secret = 'XnnLcuE5iOsrVQQZkiNJMxaz8eXHr3nizC1Halgk7v3q1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#Flask sever
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search", method = ["POST"])
def search():
    keyword = request.form.get("search_query")
    t=[]
    tweets = api.search(keyword, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.keyword).sentiment.polarity
        subjectivity = TextBlob(tweet.keyword).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
    return jsonify({"success":True,"tweets":t})
