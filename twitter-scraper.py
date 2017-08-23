import twitter
import argparse
import json

api = twitter.Api(consumer_key = 'heHwAye00lW5u9MWCRbFjQA3D',
        consumer_secret = '9cjVZkR0uOxPUE1sv2PoxvXjKjQGW0E9pucuP2jyqYUMvzWFnu',
        access_token_key = '455108134-ze0c1Tu7tl463cCAuF7XBq7n1qmvaAyUaCu75ohS',
        access_token_secret = 'M1YUCy2K94Lq9KIzI4FPTzPGHkQqfBb2LDZWQCPXlAC1H')

parser = argparse.ArgumentParser(description='Process Twitter users')
parser.add_argument('--user', metavar='U', type=str, help='user to search for')

args = parser.parse_args()
user = api.GetUser(None, args.user)
followers = api.GetFollowers(None, user) 
for follower in followers:
    print(follower.screen_name)
