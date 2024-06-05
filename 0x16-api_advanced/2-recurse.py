#!/usr/bin/python3
"""
This module contains a function to recursively fetch hot posts from
a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """
    Recursively fetches hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to fetch posts from.
        hot_list (list): A list to store the titles of hot posts.
        count (int): The number of posts fetched so far.
        after (str): The 'after' parameter for pagination.

    Returns:
        list: A list containing the titles of hot posts, or None if an error
        occurs.
    """
    base_url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "redmi_api"}
    params = {'limit': 10, 'count': count, 'after': after}

    try:
        response = requests.get(base_url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()
        if response.status_code == 404:
            raise Exception
    except requests.RequestException:
        return None

    result = response.json().get('data', {})
    after = result.get('after', None)
    count += result.get("dist")
    for post in result.get('children', []):
        hot_list.append(post.get('data', {}).get('title', None))

    if after:
        recurse(subreddit, hot_list, count, after)
    return hot_list
