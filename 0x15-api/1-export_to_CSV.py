#!/usr/bin/python3


"""
Fetches user and their to-do list data from an API, formats it into CSV
format, and saves it to a file.

Usage:
    Run the script from the command line with a user ID as an argument
    Example: python script.py 1
    This will fetch data for user with ID 1 and save it to a file named '1.csv'
"""


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
    csv_format = "\n".join(['"{0}","{1}","{2}","{3}"'.
                            format(id, username, todo.get("completed"),
                                   todo.get("title"))
                            for todo in todos])
    csv_format += "\n"
    file_name = f"{id}.csv"
    with open(file_name, "w", encoding="utf-8") as fd:
        fd.write(csv_format)
