#!/usr/bin/python3
"""
This script returns information about his/her TODO list progress
using a REST API, for a given employee ID,
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    employee = requests.get(url).json()
    url = "https://jsonplaceholder.typicode.com/todos"
    tasks = requests.get(url).json()
    total = 0
    completed = 0
    list_tasks = []
    for task in tasks:
        if task.get('userId') == employee.get('id'):
            total += 1
            if task.get('completed') is True:
                list_tasks.append(task.get('title'))
                completed += 1

    print("Employee {} is done with tasks({}/{}):".format(employee.get('name'),
                                                          completed, total))
    for item in list_tasks:
        print("\t {}".format(item))
        
