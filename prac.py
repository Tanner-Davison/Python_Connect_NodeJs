import requests
import json
import pprint
try:
    response = requests.get("http://localhost:3001/python/data-py")

    if response.status_code == 200:
        data = response.json()  
        pprint.pprint(data) 

        # Do something with the data... 

    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")