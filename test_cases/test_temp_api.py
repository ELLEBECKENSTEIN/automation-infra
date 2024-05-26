import json

import requests
from requests.auth import HTTPBasicAuth

url= 'http://localhost:3000/'
resources = 'api/teams'
user= 'admin'
password= 'admin'
header= {'Content-Type': 'application/json'}


class Test_Api_Temp:
    def test_01_create_team(self):
        payload= {"name": "Elle","email": "elle@kuku.com"}
        response=requests.post(url + resources, json=payload, headers= header, auth = HTTPBasicAuth(user, password))
        response_json= response.json()
        print(response_json)
        assert response.status_code ==200

    def test_02_get_team(self):
       response= requests.get(url + resources + '/search',  auth = HTTPBasicAuth(user, password))
       response_json = response.json()
       print(json.dumps(response_json, indent=2))
       # print(response_json)
       my_team_id=response_json['teams'][0]['id']
       print(my_team_id)
       # assert my_team_id== 2



