#!/usr/bin/python3
'''
Python script that retrieves information using a REST API
'''
import requests
import sys

def get_employee_data(employee_id):
    # API endpoint URLs
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    # Fetch employee data
    employee_data = requests.get(user_url).json()

    # Fetch employee tasks
    employee_tasks = requests.get(todos_url).json()

    return employee_data, employee_tasks

def display_todo_progress(employee_data, employee_tasks):
    # Filter completed tasks
    completed_tasks = [task for task in employee_tasks if task.get("completed")]

    # Display TODO list progress
    print(f"Employee {employee_data['name']} is done with tasks({len(completed_tasks)}/{len(employee_tasks)}):")
    
    for task in completed_tasks:
        print("\t", task["title"])

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    # Get employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Get employee data and tasks
    employee_data, employee_tasks = get_employee_data(employee_id)

    # Display TODO list progress
    display_todo_progress(employee_data, employee_tasks)

