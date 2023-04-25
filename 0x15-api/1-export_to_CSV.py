#!/usr/bin/python3
"""
This script returns information about his/her TODO list progress
using a REST API, for a given employee ID,
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    employee = requests.get(url).json()
    url = "https://jsonplaceholder.typicode.com/todos"
    tasks = requests.get(url).json()

    with open('{}.csv'.format(employee.get('id')), 'w',
              encoding='UTF8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            if task.get('userId') == employee.get('id'):
                data = [employee.get('id'), employee.get('username'),
                        task.get('completed'), task.get('title')]
                writer.writerow(data)
