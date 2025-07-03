from reddit_fetcher import fetch_posts
from response_generator import generate_response

if __name__ == "__main__":
    posts = fetch_posts()
    for post in posts:
        print("=" * 60)
        print(f"Title: {post['title']}")
        print(f"URL: {post['url']}")
        print(f"Subreddit: {post['subreddit']}, Upvotes: {post['upvotes']}, Comments: {post['comments']}")
        print(f"Context: {post['context']}")
        print("\nGenerated Response:")
        print(f"Sentiment: {post['sentiment']}, Engagement Score: {post['engagement_score']}")
        print(generate_response(post))
