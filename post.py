import requests
import json

usuario = {
  "name": "Lucas"
}

r = requests.post("http://localhost:5000/post_people", data=json.dumps(usuario))
print(r.text)