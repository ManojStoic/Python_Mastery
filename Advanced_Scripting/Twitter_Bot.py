import tweepy

# authentication method to verify your credentials
all_keys = open('D:\Work\Code\Python\Twitterbot\keys.txt','r').read().splitlines()
api_key= all_keys[0]
api_key_secret= all_keys[1]
access_token= all_keys[2]
access_token_secret= all_keys[3]

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

name = api.me()
print(name.name)