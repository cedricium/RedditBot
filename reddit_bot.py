import praw
import time
#import config
	# config file looks like the following
	# username = "<USERNAME>"
	# password = "<PASSWORD>"
	# client_id = "<CLIENT_ID> FROM REDDIT SCRIPT APP"
import os

# global variables used throughout the program
version = "v0.2"
time_to_sleep = 10
number_of_comments = 25

def bot_login():
	print "Logging in..."
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Cedric's Commenting Test Bot - v0.1")
	print "Logged in!"

	return r

def run_bot(r, comments_replied_to):
	print "Obtaining " + str(number_of_comments) + " comments..."

	for comment in r.subreddit('cedriciumCSS').comments(limit = number_of_comments):
		if "bot" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			print "String Found!"
			comment.reply("I found the string, give me a treat!")
			print "Replied to comment " + comment.id
            
            # add comment id replied to to the list
			comments_replied_to.append(comment.id)

			with open("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	print "Sleeping for " + str(time_to_sleep) + " seconds..."
	# sleep for str(time_to_sleep) seconds before running bot again
	time.sleep(time_to_sleep)

# method checks for a file with comment.id's, creates one if not found
def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")

	return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()

while True:
	run_bot(r, comments_replied_to)