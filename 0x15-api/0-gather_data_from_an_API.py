#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    api_user = f"https://jsonplaceholder.typicode.com/users/{id}"
    api_todos = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    response_user = requests.get(api_user)
    response_todos = requests.get(api_todos)
    employee_name = response_user.json().get("name")
    todos = response_todos.json()
    total_tasks = len(todos)
    completed_tasks = [
        todo.get("title") for todo in todos
        if todo.get("completed")]
    titles = "\n\t ".join(completed_tasks)
    print(f"Employee {employee_name} is done with tasks\
({len(completed_tasks)}/{total_tasks}):\n\t {titles}")
