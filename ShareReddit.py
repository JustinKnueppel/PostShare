import json
import os
import requests
from dotenv import load_dotenv
from random import choice
from twilio.rest import Client
from typing import List, TypedDict, Dict


class Person(TypedDict):
    name: str
    phone_number: str
    messages: List[str]


class RedditPost(TypedDict):
    title: str
    url: str


def get_client():
    client = Client(get_sid(), get_auth_token())
    return client


def get_sid() -> str:
    return os.environ.get("TWILIO_SID")


def get_auth_token() -> str:
    return os.environ.get("TWILIO_AUTH_TOKEN")


def get_reddit_post(subreddit: str) -> RedditPost:
    full_post = get_full_reddit_post(subreddit)
    post = get_url_and_title(full_post)
    return post


def get_full_reddit_post(subreddit: str) -> Dict:
    request = requests.get(get_top_post_url(subreddit),
                           headers={'User-agent': 'Api Call'})
    return request.json()


def get_url_and_title(full_post: Dict) -> RedditPost:
    data = get_relevant_data(full_post)
    url = data['url']
    title = data['title']
    return {'url': url, 'title': title}


def get_relevant_data(post: str) -> Dict:
    return post['data']['children'][0]['data']


def get_top_post_url(subreddit: str) -> str:
    return f'https://www.reddit.com/r/{subreddit}/top.json?t=day'


def get_people(datafile: str) -> List[Person]:
    with open(datafile) as f:
        people: List[Person] = json.load(f)

    return people


def send_message(client, phone_number, message) -> Dict:
    my_number = get_my_number()

    response = client.messages.create(
        body=message, from_=my_number, to=phone_number)
    return response


def get_my_number() -> str:
    return os.environ.get("TWILIO_MY_NUMBER")


def get_full_message(person: Person, message: str, reddit_post: RedditPost) -> str:
    full_message = f'\n\n{message} \n{reddit_post["title"]}\n{reddit_post["url"]}'
    return full_message


def main():
    load_dotenv()
    client = get_client()
    people = get_people('./people.json')
    reddit_post = get_reddit_post(subreddit='awww')

    for person in people:
        message = choice(person['messages'])
        full_message = get_full_message(person, message, reddit_post)
        response = send_message(client, person["phone_number"], full_message)
        print(f'Sent message to {person["name"]}')
        print(response)


if __name__ == '__main__':
    main()
