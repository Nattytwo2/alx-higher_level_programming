#!/usr/bin/python3
"""Python script that takes your Github credentials (username and password)
and uses the Github API to display your id"""

if __name__ == '__main__':
    import requests
    import sys
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    try:
        response = requests.get(url)
        commits = response.json()
        for commit in commits[:10]:
            print("{}: {}".format(
                commit.get('sha'),
                commit.get('commit').get('author').get('name')))
    except ValueError:
        print("Not a valid JSON")
