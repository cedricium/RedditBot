import praw
import time

# import config
# config file looks like the following
# username = "<USERNAME>"
# password = "<PASSWORD>"
# client_id = "<CLIENT_ID> FROM REDDIT SCRIPT APP"

def bot_login():
	print "Logging in..."
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Cedric's Commenting Test Bot - v0.1")
	print "Logged in!"
	return r

def run_bot(r):
	print "Obataining 25 comments..."
	for comment in r.subreddit('cedriciumCSS').comments(limit=25):
		if "bot" in comment.body:
			print "String Found!"
			comment.reply("I found the string, give me a treat!")
			print "Replied to comment " + comment.id

r = bot_login()
run_bot(r)
