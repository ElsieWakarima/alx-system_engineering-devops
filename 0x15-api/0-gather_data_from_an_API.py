#!/usr/bin/python3
"""
This script returns information about his/her TODO list progress
using a REST API, for a given employee ID,
"""

import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args_id = {'id': sys.argv[1]}
        users = requests.get("https://jsonplaceholder.typicode.com/users",
                             params=args_id).json()
        args_userId = {'userId': sys.argv[1]}
        todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                             params=args_userId).json()

        todos_len = 0
        todos_arr = []
        for i in todos:
            if i.get('completed'):
                todos_arr.append(i)
                todos_len += 1

        print("Employee {} is done with tasks({}/{}):".format(
             users[0].get('name'), todos_len, len(todos)))

        for i in todos_arr:
            print("\t {}".format(i.get('title')))
