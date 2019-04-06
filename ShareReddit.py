import requests
import info
from twilio.rest import Client
from random import choice

subreddit = 'aww'
req = requests.get(f'https://www.reddit.com/r/{subreddit}/top.json?t=day', headers = {'User-agent' : 'Justin'})
js = req.json()
url = js['data']['children'][0]['data']['url']
title = js['data']['children'][0]['data']['title']
# print(url)


client = Client(info.accountSID, info.authToken)

for person in info.people:
    message = choice(person['Messages'])
    response = client.messages.create(body=f'\n\n{message} \n{title}\n{url}', from_=info.myTwilioNumber, to=person['Phone Number'])
