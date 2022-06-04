import tweepy
import pprint

# authentication method to verify your credentials
all_keys = open('D:\Work\Code\Python\Twitterbot\keys.txt','r').read().splitlines()
api_key= all_keys[0]
api_key_secret= all_keys[1]
access_token= all_keys[2]
access_token_secret= all_keys[3]

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# api.create_friendship('twitterusername') # method to follow someone on twitter
# api. update_status('Enter the content') # method to post the tweet 
# api.update_profile(description="") # method to update the profile details
# api.get_user("Enter the name of the user") # method to fetch user details
# api.create_favourite(tweet.id) # method to like a tweet
# api.user_timeline(user_id=user.id) # method to fetch the list of tweets in other users timeline

# method to iterate the list of followers
# user1 = api.me()
# for follower in user1.followers():
#     pprint.pprint(f"{follower.name} follows {user1.name}")

# method to list the tweets in the home timeline
# tweet_home = api.home_timeline(count=20)
# for tweet in tweet_home:
#     #pprint.pprint(tweet.text) 
#     pprint.pprint(tweet.author.name.lower())

# search for keywords in twitter
# tweets = tweepy.Cursor(api.search, q='money', lang='en').items(5)
# pprint.pprint([tweet.text for tweet in tweets][2])