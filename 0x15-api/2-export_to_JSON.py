#!/usr/bin/python3
"""
This script returns information about his/her TODO list progress
using a REST API, for a given employee ID,
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    employee = requests.get(url).json()
    url = "https://jsonplaceholder.typicode.com/todos"
    tasks = requests.get(url).json()
    task_dict = {}
    new_list = []
    for task in tasks:
        new_dict = {}
        if task.get('userId') == employee.get('id'):
            new_dict['task'] = task.get('title')
            new_dict['completed'] = task.get('completed')
            new_dict['username'] = employee.get('username')
            new_list.append(new_dict)

    task_dict[employee.get('id')] = new_list
    # print(task_dict)

    with open('{}.json'.format(employee.get('id')), 'w',
              encoding='utf-8') as f:
        f.write(json.dumps(task_dict))