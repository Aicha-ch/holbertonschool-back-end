#!/usr/bin/python3
'''
Python script that retrieves information using a REST API
'''
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_data = requests.get(user_url).json()

    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    employee_tasks = requests.get(todos_url).json()

    completed_tasks = [task for task in employee_tasks if task.get("completed")]

    print(
        f"Employee {employee_data['name']} is done with "
        f"tasks({len(completed_tasks)}/{len(employee_tasks)}):"
    )
    for task in completed_tasks:
        print("\t", task["title"].replace(" ", "S").replace("\t", "T"))

