#!/usr/bin/env python3
import praw
import json
import requests


pw = [line.rstrip() for line in open('.secreto')]

reddit = praw.Reddit(client_id='8wwI5YSfA5dTXQ',
    client_secret='6OHgyygRRUa2aiJH_IfrvU0SzMo',
    username='CoolKittensCoolCats',
    password=pw,
    user_agent='catBot by /u/putthepieceawaywalte')

subreddit = reddit.subreddit('CoolKittensCoolCats')


key = {'x-api-key': 'c07bf7e3-f5bc-44f4-8da6-5f4c725e0b09'}
url = 'https://api.thecatapi.com/v1/images/search?category_ids=1' 

r = requests.get(url, key)



kw = {"I'm sad",
    "I'm having a bad day",
    "coolkittenscoolcats",
    "I need a cat",
    "my bicycle was stolen",
    "I'd like to hire Patrick McDaniel"
    }




for comment in subreddit.stream.comments(skip_existing=True):
    for k in kw:
        print("looping")
        if k.lower() in comment.body.lower():
            print("another day fixed")
            for x in r.json():
                comment.reply('{}'.format(x['url'])) 

#for comment in subreddit.stream.comments(skip_existing=True):
#    has_keyword = None
#        for k in kw:
#            if k.lower() in comment.body.lower():
#                print("another cat to the rescue")
#                
#
#for k in kw:
#    print(k)
#    for comment in subreddit.stream.comments(skip_existing=True):
#        if k.lower() in comment.body.lower():
#            print("yyyyyyyyyyyyyyyeeeeeeeeeeeesssssssss")
#            for x in r.json():
#                comment.reply('{}'.format(x['url']))
#


#for k in keywords:
#    print(k)
#    for comment in subreddit.stream.comments():
#        if k in comment.body.lower():
#            print(comment.body.lower())
#            comment.reply('{}'.format(x)

#if comment.subreddit == k:
#    print("found a match")

#for comment in subreddit.stream.comments():
#    print(comment.body.lower())
