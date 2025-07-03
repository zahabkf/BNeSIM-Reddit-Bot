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
- [License](#license)

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

pip install -r requirements.txt


