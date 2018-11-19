import twitter
import argparse
import json

api = twitter.Api(consumer_key = 'Consumer_Key',
        consumer_secret = 'consumer_secret',
        access_token_key = 'access_token',
        access_token_secret = 'secret_token')

parser = argparse.ArgumentParser(description='Process Twitter users')
parser.add_argument('--user', metavar='U', type=str, help='user to search for')

args = parser.parse_args()
user = api.GetUser(None, args.user)
followers = api.GetFollowers(None, user) 
for follower in followers:
    print(follower.screen_name)
