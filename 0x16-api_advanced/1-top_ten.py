#!/usr/bin/python3
"""
This module provides a function to retrieve and print the top ten posts from
a specified subreddit.

Functions:
    top_ten(subreddit): Retrieves and prints the top ten posts from the given
    subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Retrieve the top ten posts from a specified subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to retrieve the top posts from.
    """
    base_url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "redmi_api"}
    params = {'limit': 10}

    try:
        response = requests.get(base_url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 404:
            raise Exception
    except requests.RequestException:
        print(None)
        return

    result = response.json().get('data', {})
    index = 0
    for post in result.get('children', []):
        if index == 0:
            index += 1
            continue
        index += 1
        print(post.get('data', {}).get('title', None))
