#!/usr/bin/python3
"""
This script returns information about his/her TODO list progress
using a REST API, for a given employee ID,
"""

import requests

# function to get TODO list progress for a given employee ID
def get_employee_todo_progress(emp_id):
    # make GET request to API
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}')
    # check if response is successful
    if response.status_code == 200:
        # parse JSON response
        todo_data = response.json()
        # get employee name
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{emp_id}')
        employee_data = response.json()
        emp_name = employee_data['name']
        # count number of completed tasks
        num_completed_tasks = 0
        for task in todo_data:
            if task['completed']:
                num_completed_tasks += 1
        # display employee TODO list progress
        total_tasks = len(todo_data)
        print(f'Employee {emp_name} is done with {num_completed_tasks}/{total_tasks} tasks:')
        # display titles of completed tasks
        for task in todo_data:
            if task['completed']:
                print(f'\t{task["title"]}')

# test the function with employee ID = 1
get_employee_todo_progress(1)

