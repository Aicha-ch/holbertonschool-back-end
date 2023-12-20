#!/usr/bin/python3
'''
Python script that returns information using REST API
'''
import requests
import sys

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    employee_data = requests.get(user_url).json()
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}'
    employee_tasks = requests.get(todos_url).json()

    done_tasks = [task for task in employee_tasks if task.get("completed")]

    print(
        f"Employee {employee_data['name']} is done with "
        f"tasks({len(done_tasks)}/{len(employee_tasks)}):"
    )
    for task in done_tasks:
        print("\t", task["title"])
