import tweepy
import time
auth = tweepy.OAuthHandler('6eQ4yaYqcH6EKRP2UJZrbRqGf','CAD5OsW4psisv4IgoePlCxOfYU23W29jhIDZJTD8F3kzaTTSrA')

auth.set_access_token('905488606076207104-PfOjQ5l4bHKNgibSPl7MxhIbVo4hlbm','876vkgBEsACrFnlkzphs4bm52ddqowtluWmQ4xrot7SJN')

api = tweepy.API(auth, wait_on_rate_limit= True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Javascript'
numberTweets = 500

for tweet in tweepu.Cursor(api.search, seach).items(numberTweets):
    try:
        print('tweet liked')
        tweet.favorite()
        time.sleep(10)

    except tweepy.TweepErrora as e:
        print(e.reason)
    except StopIteration:
        break
