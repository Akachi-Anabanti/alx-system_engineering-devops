#!/usr/bin/python3
"""Defines a recursive function
that queries Reddt API"""
import requests
import time


def recurse(subreddit, hot_list=[]):
    """Calls the API with recursion
    Listing JSON responses contain `after` and `before`
    fields which are equivalent to the "next" and "prev"
    buttons on the site and in combination
    with `count` can be used to page through the listing.

    To page through a listing, start by fetching
    the first page without specifying values for `after` and `count`.
    The response will contain an `after` value
    which you can pass in the next request.
    It is a good idea, but not required,
    to send an updated value for `count` which
    should be the number of items already fetched.
    """

    headers = {"User-Agent": "ALX-SE/1.1"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        res = res.json()
        posts = res["data"]["children"]

        for post in posts:
            hot_list.append(post["data"]["title"])
        count = res["data"]["dist"]
        after_value = res["data"]["after"]

    def fetch(after_value, count):
        """The recursive function"""
        if not after_value:
            return hot_list
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?\
                after={after_value}&count={count}"
        res = requests.get(url, headers=headers, allow_redirects=False)

        if res.status_code == 200:
            res = res.json()
            posts = res["data"]["children"]

            for post in posts:
                hot_list.append(post["data"]["title"])

            count += res["data"]["dist"]

            after_value = res["data"]["after"]

            time.sleep(1)

            return fetch(after_value, count)
        else:
            return None

    return fetch(after_value, count)
