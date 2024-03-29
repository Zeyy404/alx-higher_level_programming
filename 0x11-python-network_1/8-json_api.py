#!/usr/bin/python3
"""takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter."""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}
    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
