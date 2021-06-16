#!/usr/bin/python3
"""for api"""
import json
import requests


def export_all_to_json():
    """API"""
    users_and_tasks = {}

    # do the get requests
    users_json = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    todos_json = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    user_info = {}
    for user in users_json:
        user_info[user['id']] = user['username']
    for task in todos_json:
        if users_and_tasks.get(task['userId'], False) is False:
            users_and_tasks[task['userId']] = []
        task_dict = {}
        task_dict['username'] = user_info[task['userId']]
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']

        users_and_tasks[task['userId']].append(task_dict)
    # print("users_and_tasks: {}".format(users_and_tasks))

    with open("todo_all_employees.json", 'w') as jsonFile:
        json.dump(users_and_tasks, jsonFile)

if __name__ == '__main__':
    export_all_to_json()
