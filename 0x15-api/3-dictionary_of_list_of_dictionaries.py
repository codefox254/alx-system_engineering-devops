#!/usr/bin/python3
"""This script fetches tasks from all employees and exports them to a JSON file."""

import json
import requests
import sys


def fetch_tasks():
    """Fetch tasks for all employees and create a JSON file."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_resp = requests.get(users_url)

    
    if users_resp.status_code != 200:
        print("Failed to retrieve users.")
        sys.exit(1)

    users = users_resp.json()
    users_dict = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos/'
        tasks_resp = requests.get(tasks_url)

        if tasks_resp.status_code != 200:
            print(f"Failed to retrieve tasks for user {user_id}.")
            continue

        tasks = tasks_resp.json()
        users_dict[user_id] = [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            } for task in tasks
        ]

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)

if __name__ == '__main__':
    fetch_tasks()
