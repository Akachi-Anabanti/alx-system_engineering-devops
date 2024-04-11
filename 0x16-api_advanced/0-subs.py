#!/usr/bin/python3
"""Number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the numbers of subscribers
    args:
        subreddit (str) - substring
    """

    headers = {"User-Agen": 'ALX-SE/1.1'}
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                     headers=headers,
                     allow_redirects=False)

    if r.status_code == 200:
        return r.json()['data']["subscribers"]
    return 0
