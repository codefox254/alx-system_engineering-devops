#!/usr/bin/python3
""" This script , returns information about his/her TODO list progress"""
import requests
import csv

def export_employee_todo_to_csv(employee_id):
    # Replace with the actual API endpoint URL
    api_url = f"https://api.example.com/employees/{employee_id}/todos"

    try:
        response = requests.get(api_url)
        todos = response.json()

        # Define the CSV file name
        csv_file = f"{employee_id}.csv"

        # Open the CSV file for writing
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)

            # Write the header row
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write the task information
            for task in todos:
                writer.writerow([employee_id, todos.get("employee_name"), task.get("completed"), task.get("title")])

        print(f"Data for employee ID {employee_id} has been written to {csv_file}")

    except requests.RequestException as e:
        print(f"Error fetching data from the API: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    export_employee_todo_to_csv(employee_id)

