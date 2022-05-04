#!/usr/bin/python3
import requests

# Example to call decide webhoook hosted at 192.168.1.2 Port 9000
# Features include Size and Weight

url = 'http://192.168.1.2:9000/hooks/decide'

params = {
    "Size": "32",
    "Weight": "12"
}

r = requests.get(url=url, params=params)

print(r.text)