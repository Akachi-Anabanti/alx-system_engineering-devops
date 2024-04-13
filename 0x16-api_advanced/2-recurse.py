#!/usr/bin/python3
"""Defines a recursive function
that queries Reddt API"""
import requests


def recurse(subreddit, hot_list=[], after_value=None):
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
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after_value)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        res = res.json()
        posts = res["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        after_value = res["data"]["after"]

        if not after_value:
            return hot_list
        return recurse(subreddit, hot_list, after_value)
    else:
        return None
