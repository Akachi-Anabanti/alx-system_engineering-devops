#!/usr/bin/python3
"""A script that accepts user ID and returns
Associated data"""
import sys
import urllib.request
import json


def get_todos(user_id):
    """a function that performs the API call"""
    url_tasks = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    url_user_info = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        with urllib.request.urlopen(url_user_info) as response:
            user_info = response.read().decode("utf-8")
        user_info = json.loads(user_info)
    except Exception as e:
        print(e)
        return

    try:
        with urllib.request.urlopen(url_tasks) as response:
            data = response.read().decode('utf-8')
        data = json.loads(data)
    except Exception as e:
        print(e)
        return

    total_tasks = len(data)
    tasks_completed = [task for task in data if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
            user_info.get("name"),
            len(tasks_completed),
            total_tasks
        ))

    [print(f"\t {c_task.get('title')}") for c_task in tasks_completed]


if __name__ == "__main__":
    user_id = sys.argv[1]
    get_todos(user_id)
