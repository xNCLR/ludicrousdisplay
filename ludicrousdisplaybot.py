import praw
import config
import time



print("Initialising Ludicrous Display Bot by /u/WhyDidntYouDoMyJob v0.1")

# Login details
def bot_login():
    r=praw.Reddit(username=config.username,
                password=config.password,
                client_id=config.client_id,
                client_secret=config.client_secret,
                user_agent="/u/WhyDidntYouDoMyJob's ludicrous display responder v0.1")
    return r

def run_bot(r):
    for comment in r.subreddit("all").comments(limit=150): # For every comment in the last 150 comments
    
        if "sending walcott on that early" in comment.body.lower() and comment.author!="LudicrousDisplayBot": # If the right text is found, reply to it
            print("Walcott string found!")
            comment.reply("[See, the thing about Arsenal is they always try to walk it in.](https://www.youtube.com/watch?v=gWJIQm9qH-w)")
            print("Replied to comment "+comment.id)
            print()
            time.sleep(4) # Waits so the bot doesn't double comment

        elif "ludicrous display last night" in comment.body.lower() and comment.author!="LudicrousDisplayBot": # If the right text is found, reply to it
            print("Ludicrous string found!")
            comment.reply("[What was Wenger thinking, sending Walcott on that early?](https://www.youtube.com/watch?v=gWJIQm9qH-w)")
            print("Replied to comment "+comment.id)
            print()
            time.sleep(4) # Waits so the bot doesn't double comment
         
r=bot_login()
while True:
    run_bot(r)
