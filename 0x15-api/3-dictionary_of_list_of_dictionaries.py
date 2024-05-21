#!/usr/bin/python3


"""
Fetches user and todo data from an API, associates todos with users, and saves
the result in a JSON file.

Example Usage:
    This script is executed directly, not imported as a module.
    Run the script using Python 3:
    python3 script_name.py
"""


import json
import requests


if __name__ == "__main__":

    api_user = f"https://jsonplaceholder.typicode.com/users"
    api_todos = f"https://jsonplaceholder.typicode.com/todos"
    response_user = requests.get(api_user)
    response_todos = requests.get(api_todos)
    users = response_user.json()
    todos = response_todos.json()
    content = {}
    for user in users:
        inner_list = []
        for todo in todos:
            if user.get("id") == todo.get("userId"):
                inner_dict = {"username": user.get("username"),
                              "task": todo.get("title"),
                              "completed": todo.get("completed")}
                inner_list.append(inner_dict)

        content[user.get("id")] = inner_list

    with open(f"todo_all_employees.json", "w") as fd:
        json.dump(content, fd)
