import requests
import info
from twilio.rest import Client

subreddit = 'aww'
req = requests.get(f'https://www.reddit.com/r/{subreddit}/top.json?t=day', headers = {'User-agent' : 'Justin'})
js = req.json()
url = js['data']['children'][0]['data']['url']
# print(url)


client = Client(info.accountSID, info.authToken)

message = client.messages.create(body=f'<3\n\nHere you go! {url}', from_=info.myTwilioNumber, to=info.myCellPhone)
