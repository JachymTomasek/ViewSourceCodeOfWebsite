# This program prints source code of the website at the written URL.

import requests
again = 1
while again == 1:
    url = input("url: ")
    if "http://" not in url and "https://" not in url:
        print("The given URL does not contain http:// or https://.")
        url = input("url: ")
        request = requests.get(url)
        print(request.text)
    else:
        request = requests.get(url)
        print(request.text)
    print()
    again = input("again? 1-yes, 0-no: ")
