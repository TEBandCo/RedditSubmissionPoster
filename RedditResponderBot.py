#adapted from busterttoni11 and bboe's videos. 

#changes made by /u/TheEpicBlob. 

import praw
import time

subreddit_to_search = ['SUB_TO_POST_TO '] #list of subreddits to search and comment on,comma separated
comment_to_reply_with = "this is a test" #comment to reply with, use triple quotes for multiline


def authenticate():
    print("Authenticating..."),
    reddit = praw.Reddit('PRAW_FILE', #see praw.ini file
        user_agent="PROVIDE DETAILS OF YOUR BOT HERE") #provide description of bot
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit



def main():
    reddit = authenticate()
    while True:
        run_bot(reddit)


def run_bot(reddit):
    print("Getting comments...")
    for sub in subreddit_to_search:
        for submission in reddit.subreddit(sub).stream.submissions(skip_existing=True):
            if submission.author.name !=reddit.user.me(): 
                print("New submission! " + submission.id)
                submission.reply(comment_to_reply_with)
                print("Replied to " + submission.id)
                print("Waiting for 10 seconds")
                time.sleep(10)


if __name__ == '__main__':
    main()
