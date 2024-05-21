#!/usr/bin/python3


"""
Fetches user and their to-do list data from an API, formats it into JSON
format, and saves it to a file.

Usage:
    Run the script from the command line with a user ID as an argument
    Example: python script.py 1
    This will fetch data for user with ID 1 and save it to a file named
    '1.json'
"""


import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    api_user = f"https://jsonplaceholder.typicode.com/users/{id}"
    api_todos = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    response_user = requests.get(api_user)
    response_todos = requests.get(api_todos)
    username = response_user.json().get("username")
    todos = response_todos.json()
    inner_list = []

    for todo in todos:
        inner_dict = {"task": todo.get("title"),
                      "completed": todo.get("completed"),
                      "username": username}
        inner_list.append(inner_dict)

    content = {id: inner_list}

    with open(f"{id}.json", "w") as fd:
        json.dump(content, fd)
