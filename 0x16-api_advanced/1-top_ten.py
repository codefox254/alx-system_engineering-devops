#!/usr/bin/python3
"""
Contains the function top_ten that queries the Reddit API
"""

import requests
from sys import argv

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.

    Args:
        subreddit (str): The name of the subreddit to query.
    
    Prints:
        The titles of the first 10 hot posts, or None if the subreddit is invalid.
    """
    user = {'User-Agent': 'Mozilla/5.0 (compatible; CustomBot/1.0)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    
    try:
        response = requests.get(url, headers=user, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data').get('children')
            for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)
    except Exception:
        print(None)

if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
