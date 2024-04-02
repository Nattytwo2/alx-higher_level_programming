#!/usr/bin/python3
"""Python script that  takes in a URL and an email, sends a POST URL"""
if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
