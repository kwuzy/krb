import praw
import time

while True:
    r = praw.Reddit('krb')
    subreddit = r.subreddit('pennystocks')
    thread = r.submission(id='71harf')
    for post in subreddit.top('day'):
        thread.reply(post.score)

    time.sleep(20)
