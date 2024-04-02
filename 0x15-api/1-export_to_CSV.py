#!/usr/bin/python3
"""A script that accepts user ID and returns
Associated data"""
import csv
import json
import sys
import urllib.request


def to_csv(user_id):
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
    with open(f"{user_id}.csv", "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        lines = [
                    [
                        user_id,
                        user_info.get('username'),
                        task.get("completed"),
                        task.get("title")
                    ]
                    for task in data
                ]
        writer.writerows(lines)


if __name__ == "__main__":
    user_id = sys.argv[1]
    to_csv(user_id)
