#!/usr/bin/python3
"""
Contains the function count_words that queries the Reddit API
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None, count_dict={}):
    """
    Queries the Reddit API, parses the titles of all hot articles, and prints a sorted

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): The list of keywords to count in the titles.
        hot_list (list): The list of hot article titles (used for recursion).
        after (str): The pagination parameter for the next page of results.
        count_dict (dict): A dictionary to store the count of keywords.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
