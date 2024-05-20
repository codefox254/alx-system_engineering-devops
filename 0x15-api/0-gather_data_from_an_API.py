#!/usr/bin/python3
""" This script , returns information about his/her TODO list progress"""
import requests

def get_employee_todo_progress(employee_id):
    # Replace with the actual API endpoint URL
    api_url = f"https://api.example.com/employees/{employee_id}/todos"

    try:
        response = requests.get(api_url)
        response_data = response.json()

        # Extract relevant information
        employee_name = response_data.get("employee_name")
        total_tasks = len(response_data.get("todos"))
        done_tasks = sum(1 for task in response_data.get("todos") if task.get("status") == "Done")

        # Print the progress
        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        for task in response_data.get("todos"):
            if task.get("status") == "Done":
                print(f"\t{task.get('title')}")

    except requests.RequestException as e:
        print(f"Error fetching data from the API: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)


