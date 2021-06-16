#!/usr/bin/python3
""" Write a Python script that, using this REST API """
import sys
import requests
import sys


def get_employee_tasks(employeeId):
    # print(employeeId);
    # variables
    name = ''
    task_list = []
    completed_counter = 0

    # Do the Get requests
    usersRes = requests.get('https://jsonplaceholder.typicode\
                           .com/users/{}'.format(employeeId))
    todosRes = requests.get('https://jsonplaceholder.typicode.\
                            com/users/{}/todos'.format(employeeId))
    # print("usersRes: {}\n".format(usersRes))
    # print("todosRes: {}\n".format(todos))

    # Get the JSON from responses
    name = usersRes.json().get('name')
    # print("Name: {}".format(name))
    todosJson = todosRes.json()
    # print("todosJson: {}".format(todosJson))
    # loop the tasks
    for task in todosJson:
        # up the counter if completed
        if task.get('completed') is True:
            completed_counter += 1
            # save task title to task_list
            task_list.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed_counter, len(todosJson)))

    for task in task_list:
        print('\t {}'.format(task))
    # print("task_list: {}".format(task_list))
    # Print first line
    # print()
    return 0

if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
