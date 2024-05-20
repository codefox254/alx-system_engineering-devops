#!/usr/bin/python3
# This script fetches tasks from all employees and exports them to a JSON file.

import requests
import json

def export_all_employees_todo_to_json():
    # Replace with the actual API endpoint URL
    api_url = "https://api.example.com/todos"

    try:
        response = requests.get(api_url)
        todos = response.json()

        # Create a dictionary to store tasks for all employees
        all_tasks_dict = {}

        # Populate the dictionary with task information
        for task in todos:
            user_id = task.get("userId")
            if user_id not in all_tasks_dict:
                all_tasks_dict[user_id] = []
            task_info = {
                "username": task.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            all_tasks_dict[user_id].append(task_info)

        # Define the JSON file name
        json_file = "todo_all_employees.json"

        # Write the dictionary to a JSON file
        with open(json_file, 'w') as file:
            json.dump(all_tasks_dict, file, indent=4)

        print(f"Data for all employees has been written to {json_file}")

    except requests.RequestException as e:
        print(f"Error fetching data from the API: {e}")

if __name__ == "__main__":
    export_all_employees_todo_to_json()

