import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

def analyze(handle):
    twitter_consumer_key = 'CONSUMER_KEY'
    twitter_consumer_secret = 'CONSUMER_SECRET'
    twitter_access_token = 'ACCESS_TOKEN'
    twitter_access_secret = 'ACCESS_SECRET'
    twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                             consumer_secret=twitter_consumer_secret,
                             access_token_key=twitter_access_token,
                             access_token_secret=twitter_access_secret)

    statuses = twitter_api.GetUserTimeline(screen_name=handle,
    count=200, include_rts=False)

    text = ""

    for status in statuses:
        if (status.lang =='en'): #English tweets only
            text += status.text.encode('utf-8')

    #The IBM Bluemix credentials for Personality Insights!
    pi_username = 'PI_USERNAME'
    pi_password = 'PI_PASSWORD'

    personality_insights = PersonalityInsights(username=pi_username, password=pi_password)

    pi_result = personality_insights.profile(text)

    return pi_result