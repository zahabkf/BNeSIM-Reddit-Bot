import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def generate_response(post):
    """
    Generate a helpful, natural response to a Reddit post
    that subtly promotes BNESIM and follows community tone.
    """

    prompt = f"""
You are replying to a Reddit post in the subreddit r/{post['subreddit']}.
The post is about travel connectivity or international eSIMs.

Here is the post:
---
Title: {post['title']}
Content: {post['content']}
---

Your task is to write a genuine, non-pushy Reddit-style comment that:
- Addresses the user's specific question or concern
- Offers helpful advice or personal experience
- Mentions BNESIM naturally as a solution or option
- Avoids sounding like a sales pitch or bot
- Follows Reddit etiquette and adds value to the conversation
- **Avoids using exclamation marks (!)** to keep the tone natural

Avoid using overly formal language. Sound friendly, informed, and helpful.

Now write the response:
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[ERROR generating response: {e}]"
