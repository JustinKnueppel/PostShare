# Post Sharing

Use Reddit API to share posts via the Twilio API

## Docker

Relies on docker running on current system

# To set up cron job

```
crontab -e
```

Add the following line to the crontab

```
0 10 * * * /path/to/PostShare/automate.sh
```

# people.json

```
[
  {
    "name": "John Doe",
    "phone_number": "12348675309"
    "messages": [
      "Hello",
      "World"
    ]
  }
]
```

# .env

```
TWILIO_SID=<your sid>
TWILIO_AUTH_TOKEN=<your auth token>
TWILIO_MY_NUMBER=<your number>
```
