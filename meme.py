import praw
import random
def dank():
    reddit = praw.Reddit(client_id ='your client id of reddit app',
                         client_secret ='your client secret of reddit app' ,
                         username='your reddit username',
                         password='your reddit pass',
                         user_agent='meme.exe')

    subreddit = reddit.subreddit('dankmemes')

    hot_memes = subreddit.new(limit=2)

    links=[]

    for submission in hot_memes:
        #if 'jpg' in submission.url or 'png' in  submission.url:
        links.append((submission.url,submission.title))
    random.shuffle(links)        
    return random.choice(links)

def normie_meme():
    reddit = praw.Reddit(client_id ='your client id of reddit app',
                         client_secret ='your client secret of reddit app' ,
                         username='your reddit username',
                         password='your reddit pass',
                         user_agent='meme.exe')

    subreddit = reddit.subreddit('memes')

    hot_memes = subreddit.new(limit=2)

    links=[]

    for submission in hot_memes:
        #if 'jpg' in submission.url or 'png' in  submission.url:
        links.append((submission.url,submission.title))
    random.shuffle(links)        
    return random.choice(links)

def dank_meme():
    reddit = praw.Reddit(client_id ='your client id of reddit app',
                         client_secret ='your client secret of reddit app' ,
                         username='your reddit username',
                         password='your reddit pass',
                         user_agent='meme.exe')

    subreddit = reddit.subreddit('dankmemes')

    hot_memes = subreddit.new(limit=2)

    links=[]

    for submission in hot_memes:
        #if 'jpg' in submission.url or 'png' in  submission.url:
        links.append((submission.url,submission.title))
    random.shuffle(links)        
    return random.choice(links)

def stonks_meme():
    reddit = praw.Reddit(client_id ='your client id of reddit app',
                         client_secret ='your client secret of reddit app' ,
                         username='your reddit username',
                         password='your reddit pass',
                         user_agent='meme.exe')

    subreddit = reddit.subreddit('MemeMan')

    hot_memes = subreddit.new(limit=7)

    links=[]

    for submission in hot_memes:
        #if 'jpg' in submission.url or 'png' in  submission.url:
        links.append((submission.url,submission.title))
    random.shuffle(links)        
    return random.choice(links)
def edgy_meme():
    reddit = praw.Reddit(client_id ='your client id of reddit app',
                         client_secret ='your client secret of reddit app' ,
                         username='your reddit username',
                         password='your reddit pass',
                         user_agent='meme.exe')

    subreddit = reddit.subreddit('im14andthisisdeep')

    hot_memes = subreddit.new(limit=2)

    links=[]

    for submission in hot_memes:
        #if 'jpg' in submission.url or 'png' in  submission.url:
        links.append((submission.url,submission.title))
    random.shuffle(links)        
    return random.choice(links)
