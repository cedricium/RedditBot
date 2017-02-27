import praw			# reddit api wrapper for python
import config		# configuration file for logging into reddit
import time			# for counting purposes
import os			# reading / writing contents to files on computer
import fileinput	# used to add text to existing file
import subprocess	# used to execute bash script

# variables used throughout the program
version = "v1.0"
time_to_sleep = 15
number_of_comments = 500

def bot_login():
	print "Logging in..."
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Cedricium's Personal Assistant Bot: saves links on command to a file on GitHub - " + version)
	print "Logged in!"

	return r

def run_bot(r, comments_replied_to, saved_reddit_links):
	for comment in r.redditor('Cedricium').comments.new(limit=10):
		if "!save" in comment.body and comment.id not in comments_replied_to:
			print("Match for '!save' found!")
			
			command,tag = comment.body.split(" - ")

			submission_title = comment.link_title
			submission_url = comment.link_url
			
			# comment.reply("Hey Cedricium, I will be saving this thread under the `" + tag + "` tag. Have a good one!\n\n&nbsp;\n\n---\n^G'day, ^I ^am ^a ^personal ^assistant ^bot.\n\n**^Source ^Code:** [^Here ^on ^GitHub](https://github.com/cedricium/RedditBot)^.\n\n**^Created ^By:** ^/u/Cedricium")
			
			tag_and_title = "## " + tag + "\n  * [" + submission_title + "](" + submission_url + ")\n"
			
			title_only = "\n  * [" + submission_title + "](" + submission_url + ")\n"	
			
			# add tag, title, and URL to docs/index.md
			if tag.encode('utf-8') not in open("docs/index.md").read():
				saved_reddit_links.append(tag_and_title)

				with open("docs/index.md", "a") as f:
					s = ""
					seq = (tag_and_title, "\n")
					f.write(s.join(seq).encode('utf-8'))
			else:
				for line in fileinput.FileInput("docs/index.md",inplace=1):
					if tag.encode('utf-8') in line:
						line = line.replace(line,line + title_only.encode('utf-8'))
					print line,

			# add comment.id to comments_replied_to
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


# method checks for a file with saved links, creates one if not found
def get_saved_links():
	if not os.path.isfile("docs/index.md"):
		saved_reddit_links = []
	else:
		with open("docs/index.md", "r") as f:
			saved_reddit_links = f.read()
			saved_reddit_links = saved_reddit_links.split("\n")

	return saved_reddit_links


r = bot_login()
comments_replied_to = get_saved_comments()
saved_reddit_links = get_saved_links()

while True:
	run_bot(r, comments_replied_to, saved_reddit_links)
	subprocess.call("./push_to_github.sh", shell=True)