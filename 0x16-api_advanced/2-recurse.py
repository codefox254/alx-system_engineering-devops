#!/usr/bin/python3
"""
Contains the function count_words that queries the Reddit API
and prints a sorted count of given keywords in the titles of all hot articles.
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None, count_dict={}):
    """
    Queries the Reddit API, parses the titles of all hot articles, and prints a sorted
    count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): The list of keywords to count in the titles.
        hot_list (list): The list of hot article titles (used for recursion).
        after (str): The pagination parameter for the next page of results.
        count_dict (dict): A dictionary to store the count of keywords.

    Returns:
        None
    """
    user = {'User-Agent': 'Mozilla/5.0 (compatible; CustomBot/1.0)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=user, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data').get('children')
            for post in posts:
                title = post.get('data').get('title').lower().split()
                hot_list.extend(title)
            after = data.get('data').get('after')
            if after:
                return count_words(subreddit, word_list, hot_list, after, count_dict)
            else:
                word_list = [word.lower() for word in word_list]
                for word in word_list:
                    count_dict[word] = count_dict.get(word, 0) + hot_list.count(word)
                sorted_counts = sorted(count_dict.items(), key=lambda item: (-item[1], item[0]))
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return
    except requests.RequestException:
        return
