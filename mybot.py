import praw
import pdb
import re
import os
import datetime

USER_AGENT = "raspi:dont_step_on_snek:v1.0.0"

if not os.path.isfile("posts_replied_to.txt"):
	posts_replied = []
else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

#now = datetime.datetime.now(datetime.timezone.utc)
reddit = praw.Reddit(client_id='uKPkv1o4Qrmc_w',
                   client_secret='nyNSzrlaS0kna1zc7Cj8r6dyHMU',
                   username='bot_test7890',
                   password='Pass2019',
		     user_agent='USER_AGENT')

##      with open("posts_replied_to.txt", "r") as file:
##              posts_replied_to = file.read()
##              posts_replied_to = posts_replied_to.split("\n")
##              posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('pythonforengineers')
message=("checkum.")
for comment in subreddit.stream.comments():
	if comment.author != "bot_test7890":
		if comment.id not in posts_replied_to:
			try:
				print(comment.body)
	        	       	if re.search("dubs", comment.body, re.IGNORECASE):
#	        	               	message=("checkum")
	                	        comment.reply(message)
	                        	print("bot replying to:  " +  comment.id)
					with open("posts_replied_to.txt", "a") as file:
	                                        file.write("comment ID: " + comment.id + "\n" + "Comment Body: " + comment.body + "\n" + "Reply: " + message + "\n =========================================")

			except APIException as e:
				print("error!")

	#	        with open("posts_replied_to.txt", "a") as file:
	#				file.write("comment ID: " + comment.id + "\n" + "Comment Body: " + comment.body + "\n" + "Reply: " + message + "\n ================================================= \n")
