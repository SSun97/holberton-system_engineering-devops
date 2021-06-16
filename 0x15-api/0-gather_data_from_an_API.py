#!/usr/bin/python3
"""This module returns employee task information"""
import requests
from sys import argv


if __name__ == "__main__":

    count = 0
    task_list = []

    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(argv[1]))

    name = userRes.json().get('name')
    tasks = todosRes.json()

    for task in tasks:
        if task.get('completed') is True:
            count += 1
            task_list.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(name, count, len(tasks)))

    for task in task_list:
        print('\t {}'.format(task))
