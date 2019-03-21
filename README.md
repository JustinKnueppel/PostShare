## Post Sharing

Use Reddit API to share posts

# To set up venv

```
python -m venv env
pip install -r requirements.txt
```

# To set up cron job

```
crontab -e

* 10 * * * cd /path/to/PostShare;source env/bin/activate;python ShareReddit.py
```

# info.py

```
accountSID = 'xxxMyAccountSIDxxx'
authToken = 'xxxMyAuthTokenxxx'
myTwilioNumber = 'xxxMyTwilioNumberxxx'
person1 = {'Phone Number' : '+1234567890', 'Messages' : ['Message 1', 'Message 2']}
person2 = {'Phone Number' : '+12223334444', 'Messages' : ['Message 1', 'Message 2']}
people = [person1, person2]
```
