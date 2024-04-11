#!/usr/bin/python3
"""Defines a function that
prints the first 10 hot
posts"""
import requests


def top_ten(subreddit):
    """Gets the top 10 hot posts"""

    header = {"User-Agent": "ALX-SE/1.1"}
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9",
                     headers=header,
                     allow_redirects=False)
    if r.status_code == 200:
        posts = r.json()["data"]["children"]

        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
