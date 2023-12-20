#!/usr/bin/python3
"""Export data in JSON format and print TODO list progress"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(argv[1]))
    user_data = user_response.json()

    tasks_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(argv[1]))
    todo_data = tasks_response.json()

    username = user_data.get("username")
    user_id = argv[1]

    tasks = []
    completed_tasks = []
    for task in todo_data:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        tasks.append(task_dict)
        if task.get('completed'):
            completed_tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(username,
                                                          len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task))

    todos = {user_id: tasks}

    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(todos, jsonfile)
