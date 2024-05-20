#!/usr/bin/python3
"""This file Records all tasks that are owned by this employee"""
import requests
import json

def export_employee_todo_to_json(employee_id):
    # Replace with the actual API endpoint URL
    api_url = f"https://api.example.com/employees/{employee_id}/todos"

    try:
        response = requests.get(api_url)
        todos = response.json()

        # Create a dictionary to store the tasks
        tasks_dict = {employee_id: []}

        # Populate the dictionary with task information
        for task in todos:
            task_info = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": todos.get("employee_name")
            }
            tasks_dict[employee_id].append(task_info)

        # Define the JSON file name
        json_file = f"{employee_id}.json"

        # Write the dictionary to a JSON file
        with open(json_file, 'w') as file:
            json.dump(tasks_dict, file, indent=4)

        print(f"Data for employee ID {employee_id} has been written to {json_file}")

    except requests.RequestException as e:
        print(f"Error fetching data from the API: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    export_employee_todo_to_json(employee_id)

