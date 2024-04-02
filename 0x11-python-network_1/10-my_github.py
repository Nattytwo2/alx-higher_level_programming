#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter"""

if __name__ == '__main__':
    import requests
    import sys
    authorize = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user', auth=authorize)
    try:
        print(response.json().get('id'))
    except ValueError:
        print("Not a valid JSON")
