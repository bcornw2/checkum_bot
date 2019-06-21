import praw
import pdb
import re
import os
import datetime

now = datetime.datetime.now(datetime.timezone.utc)
reddit = new.praw(client_id='uKPkv1o4Qrmc_w',
                   client_secret='nyNSzrlaS0kna1zc7Cj8r6dyHMU',
                   username='bot_test7890',
                   password='Pass2019')

##      with open("posts_replied_to.txt", "r") as file:
##              posts_replied_to = file.read()
##              posts_replied_to = posts_replied_to.split("\n")
##              posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('pythonforengineers')

for comment in subreddit.stream.comments():
        if comment.author != "bot_test7890":
##                if age > 259200:
                        print(comment.body)
                        if re.search("dubs", comment.body, re.IGNORECASE):
                                message=("checkum")
                                comment.reply(message)
                                print("bot replying to:  ", comment.id)


##                      posts_replied_to.append(comment.id)


        with open("posts_replied_to.txt", "w") as file:
#                file.write(url + "\t")
 #               file.write(comment.id + "\n")
  #              file.write(comment.body + "\n")
   #             file.write("============================= \n")


		file.write(comment.id + "\n" + comment.body + "\n" + "Reply: " + message + "\n ================================================= \n")
