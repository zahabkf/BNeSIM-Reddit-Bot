# BNESIM Reddit AI Automation Bot

This Python-based automation tool identifies, extracts and analyzes Reddit discussions related to travel connectivity, international roaming, and eSIMs. It then generates context aware, human like reply suggestions using Google's Gemini API. The goal is to help BNESIM identify high-quality marketing opportunities and engage users authentically on Reddit.

---

## Table of Contents

- [Purpose](#purpose)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Example Output](#example-output)
- [Challenges Faced](#challenges-faced)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

---

## Purpose

To discover and engage with Reddit users who are actively discussing travel SIMs, roaming issues, or related challenges. This tool automates the discovery, evaluation, and response suggestion process, enabling efficient, non intrusive engagement with potential users.

---

## Features

- Reddit post discovery from relevant travel and tech subreddits
- Keyword filtering and time-window constraints to identify relevant posts
- Extraction of filtered and identified reddit posts
- Sentiment analysis using NLTK's VADER to determine user tone
- Engagement prediction based on upvotes and comment volume
- Context classification (e.g., question vs. statement)
- Response generation using Gemini API with customized prompts to avoid salesy language
- Modular architecture with clean separation between functionality components

---

## Project Structure

bnesim-reddit-bot/
│
├── main.py # Main script that runs the full pipeline
├── reddit_fetcher.py # Fetches Reddit posts using PRAW
├── response_generator.py # Generates AI-based responses via Gemini API
├── analysis_utils.py # Sentiment analysis and engagement scoring
├── config.py # Environment variable loading from .env
├── .env # Private API keys (excluded from version control)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/zahabkf/bnesim-reddit-bot.git
cd bnesim-reddit-bot
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the environment

- Create a Reddit app via https://www.reddit.com/prefs/apps ,Choose “script” type to get the client_id, client_secret, user_agent keys
- Follow this link https://aistudio.google.com/apikey , click on "Create API Key" to get Gemini API Key
- Replace the place holders in the .env file as seen below with the API keys (Note: Do not include quotes around the values.)

```ini
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_user_agent_string
GEMINI_API_KEY=your_google_generativeai_key
```

### 4. Run the code

- If code does not run properly and doesn't generate an output then : 
1. Run the config.py file
2. Run the analysis_utils.py file
3. Run the reddit_fetcher.py file
4. Run the respone_generator.py file
5. Run the main.py file

Note: These files only need to be run separately in the beginning, afterwards only the main.py needs to be run if required.

## Example Output

![WhatsApp Image 2025-07-03 at 5 00 01 AM](https://github.com/user-attachments/assets/c320db84-8460-4c27-bfd4-b399d5713b68)

![WhatsApp Image 2025-07-03 at 5 00 30 AM](https://github.com/user-attachments/assets/ef503ed7-8ed3-4487-85f9-962fd7bab867)

## Challenges faced

- Reddit API rate limits slowed large-scale subreddit scanning
- Keyword-based matching missed some semantically relevant posts
- Tuning Gemini prompts to sound natural while remaining informative
- Varying Reddit post formats required flexible handling
- Sentiment analysis struggled with sarcasm and short-form posts
- API limits on Gemini's free tier required prompt length control

## Future Improvements

- Integrate semantic search (e.g., using embeddings) for smarter post discovery
- Implement a front-end dashboard for reviewing and approving AI responses
- Add persistent logging of replies and outcomes
- Deploy as a scheduled task or serverless function
- Add translation support for international subreddits

## Credits

This code was created solely by Zahab Khan and only Zahab Khan for testing purposes with BNeSIM.
