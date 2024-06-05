#!/usr/bin/python3
"""
This module provides a function to retrieve the number of subscribers for
a given subreddit.

The `number_of_subscribers` function queries the Reddit API to get
the subscriber count
for a specified subreddit. If the subreddit does not exist or the request
is redirected,
the function returns 0.

Functions:
    number_of_subscribers(subreddit): Returns the number of subscribers for
    the given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    This function queries the Reddit API to retrieve the number of subscribers
    for the specified subreddit. If the subreddit does not exist or the request
    is redirected to a search page, the function returns 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit
        does not exist or the request is redirected.
    """
    base_url = "https://api.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "redmi_api"}

    try:
        response = requests.get(base_url, headers=headers,
                                allow_redirects=False)
        response.raise_for_status()
    except requests.RequestException:
        return 0

    if response.status_code == 404:
        return 0

    return response.json().get("data", {}).get("subscribers", 0)
