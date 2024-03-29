#!/usr/bin/python3
"""takes 2 arguments in order to list 10 commits
   (from the most recent to oldest) using the GitHub API"""
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)

    commits = response.json()

    try:
        for index in range(10):
            commit = commits[index]
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
