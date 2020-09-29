# Post Sharing

Use Reddit API to share posts via the Twilio API

## Docker

Relies on docker running on current system

# To set up cron job

```bash
crontab -e
```

Add the following line to the crontab

```nohilight
0 10 * * * /path/to/PostShare/automate.sh
```

# people.json

```json
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

```bash
TWILIO_SID=<your sid>
TWILIO_AUTH_TOKEN=<your auth token>
TWILIO_MY_NUMBER=<your number>
```

# Terraform

Need to add environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

Run

```bash
pip install --target src -r requirements.txt
cd infrastructure
terraform init
terraform plan
```
