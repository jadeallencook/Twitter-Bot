#importing requirments
from time import sleep
from DataManager import BotSql
import tweepy


#setting api keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret_token = ''

#authorizing & setting up api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret_token)
auth.secure = True
api = tweepy.API(auth)

#define bot
myBot = api.me()
botsql = BotSql()

#Show information
print('Connected as: @' + myBot.screen_name + '\n Current database stats: \n' + botsql.get_stats())