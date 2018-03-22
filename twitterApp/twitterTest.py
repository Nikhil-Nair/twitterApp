import requests
from requests_oauthlib import OAuth1

def inputTweetName():
    APIKey = ''
    APISecret = ''
    AccessToken = ''
    AccessTokenSecret = ''

    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

    auth = OAuth1(APIKey, APISecret, AccessToken, AccessTokenSecret)
    username = input("Enter Handle")
    verificationUrl = 'https://api.twitter.com/1.1/users/show.json?screen_name=%s' %username
    response = requests.get(verificationUrl, auth=auth)
    if response.status_code == 200:
        printTweets(username, auth)
    else:
        print("Invalid Handle!")

def printTweets(username, auth):
    requestUrl = ' https://api.twitter.com/1.1/statuses/user_timeline.json?tweet_mode=extended&screen_name=%s&count=10' %username
    r = requests.get(requestUrl, auth=auth)
    for tweet in r.json():
        print (tweet['full_text'])
        print(tweet)
        print("\n")

inputTweetName()
