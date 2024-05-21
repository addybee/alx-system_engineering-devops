#!/usr/bin/python3


"""
Fetches and displays information about a user's tasks from an API based on
a user ID provided via command line argument.

Example Usage:
```python
# Run the script from the command line with a user ID
python script.py 1
```

Inputs:
- sys.argv[1]: User ID passed as a command line argument.

Flow:
1. Retrieves the user ID from the command line.
2. Constructs two API URLs to fetch user details and their todo tasks.
3. Makes HTTP GET requests to these URLs.
4. Processes the JSON responses to calculate the number of completed tasks
and formats them.
5. Prints the employee's name and their task completion status.

Outputs:
- Prints the employee's name and a summary of their completed tasks.
"""


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
