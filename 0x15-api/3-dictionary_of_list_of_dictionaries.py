#!/usr/bin/python3
"""A script that accepts user ID and returns
Associated data"""
import csv
import json
import sys
import urllib.request


def get_all():
    """gets all user info"""

    url_users_info = "https://jsonplaceholder.typicode.com/users/"

    try:
        with urllib.request.urlopen(url_users_info) as response:
            users_info = response.read().decode("utf-8")
        users_info = json.loads(users_info)
    except Exception as e:
        print(e)
        return

    info = dict()
    for user in users_info:
        list_of_tasks = to_json(user.get("id"))
        info.update({user.get("id"): list_of_tasks})
    with open("todo_all_employees.json", "w") as file:
        json.dump(info, file)


def to_json(user_id):
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
    list_of_tasks = [
                        {
                            "username": user_info.get("username"),
                            "task": task.get("title"),
                            "completed": task.get("completed"),
                        }
                        for task in data
                    ]

    return list_of_tasks


if __name__ == "__main__":
    get_all()
