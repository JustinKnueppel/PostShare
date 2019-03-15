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
