#!/usr/bin/python3
"""
This script returns information about his/her TODO list progress
using a REST API, for a given employee ID,
"""

import requests
import sys

if __name__ == '__main__':
    def get_employee_todo_progress(emp_id):
        response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}')
        if response.status_code == 200:
            todo_data = response.json()
            response = requests.get(f'https://jsonplaceholder.typicode.com/users/{emp_id}')
            employee_data = response.json()
            emp_name = employee_data['name']
            num_completed_tasks = 0
            for task in todo_data:
                if task['completed']:
                    num_completed_tasks += 1
            total_tasks = len(todo_data)
            print(f'Employee {emp_name} is done with {num_completed_tasks}/{total_tasks} tasks:')
            for task in todo_data:
                if task['completed']:
                    print(f'\t{task["title"]}')

    get_employee_todo_progress(sys.argv[1])
