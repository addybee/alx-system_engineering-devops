#!/usr/bin/python3
"""
This module contains a function to count the occurrences of words in the titles
of hot posts from a given subreddit.
"""

import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    Recursively counts the occurrences of words in the titles of hot posts
    from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): A list of words to count in the titles.
        instances (dict, optional): A dictionary to store the count of words.
            Defaults to an empty dictionary.
        after (str, optional): The 'after' parameter for pagination. Defaults
        to an empty string.
        count (int, optional): The count of posts processed so far. Defaults
        to 0.

    Returns:
        None: Prints the word counts sorted by count in descending order and
        then alphabetically.
    """
    url = "https://api.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "redmi_api"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")

    for post in results.get("children"):
        title = post.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
