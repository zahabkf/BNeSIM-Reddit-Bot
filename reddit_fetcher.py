import praw
import random
from datetime import datetime, timedelta
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
from analysis_utils import analyze_sentiment

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

KEYWORDS = [
    "travel esim", "international roaming", "roaming charges",
    "BNESIM", "airalo", "nomad esim", "holafly", "connectivity while traveling",
    "best esim for travel", "data sim for travel"
]

def fetch_posts(subreddits=["travel", "solotravel", "digitalnomad", "onebag", "backpacking", "eSIMs", "femaletravels", "Europetravel", "TravelHacks"], days=7):
    posts = []
    for subreddit in subreddits:
        submissions = reddit.subreddit(subreddit).top(time_filter="week", limit=100)
        for submission in submissions:
            created_time = datetime.utcfromtimestamp(submission.created_utc)
            if created_time > datetime.utcnow() - timedelta(days=days):
                content = (submission.title + " " + (submission.selftext or "")).lower()
                if any(keyword in content for keyword in KEYWORDS):
                    sentiment = analyze_sentiment(content)
                    engagement_score = submission.score + (submission.num_comments * 2)

                    posts.append({
                        "title": submission.title,
                        "content": submission.selftext,
                        "url": submission.url,
                        "subreddit": submission.subreddit.display_name,
                        "upvotes": submission.score,
                        "comments": submission.num_comments,
                        "context": "question" if "?" in submission.title.lower() else "statement",
                        "sentiment": sentiment,
                        "engagement_score": engagement_score
                    })

    #sort by engagement first
    posts.sort(key=lambda p: p["engagement_score"], reverse=True)


    # Return at least 3 posts
    return posts[:5]
