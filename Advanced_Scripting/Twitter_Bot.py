import tweepy

# authentication method to verify your credentials
auth = tweepy.OAuthHandler('lFnasNk72YkMD7PrU8qo0bqOJ', '5S6w2QRhIqOqqdOzADB6YNSRUB7cjWGwMeTivhH8GARw2APxfR')
auth.set_access_token('835379383120592897-RHR5SIDDDptK2eGrNAItw2tZqHpjrKP', 'bcXMD3EYk5GUH3NYzm7aUNy2u1MhfHCAoPYDO4EzzU0vw')

api = tweepy.API(auth)

name = api.me()
print(name.name)