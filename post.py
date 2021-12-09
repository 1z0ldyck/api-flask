# module for posting on the api

import requests
import json

usuario = {
  "name": "Lucas",
  "age": 20
}

# post person data in api
r = requests.post("http://localhost:5000/post_people", data=json.dumps(usuario))

# print message if get error in api
if(r.status_code == 500):
  print(r.text)