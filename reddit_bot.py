import praw
import config
import time
import requests

def bot_login():
# log into the reddit account with credentials from config.py
	r = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "chuck norris bot v1.0")
	return r

def run_bot(r):
# run the bot on subreddit designated in config.py
	for comment in r.subreddit(config.sub_reddit).comments(limit = 25):
		comment.body = comment.body.lower()
		if "chuck norris" in comment.body and comment.author != config.username:
			print "Chuck Norris mentioned!"
			joke_json = requests.get("https://api.icndb.com/jokes/random").json()
			joke = str(joke_json['value']['joke'])
			if joke.split(" ")[0] != "Chuck":
				joke = joke[0].lower() + joke[1:]
			comment.reply("""You seem to know a lot about Chuck Norris, but 
				did you know that """ + joke + +"""\nThis fact brought
				 to you by [icndb.com](http://www.icndb.com/)
				""")
			time.sleep(10)

r = bot_login()
while True:
	run_bot(r)