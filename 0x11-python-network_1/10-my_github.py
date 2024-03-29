#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
   and uses the GitHub API to display your id"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    user_data = response.json()
    user_id = user_data['id']
    print(user_id)
