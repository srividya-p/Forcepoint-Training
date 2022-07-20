import requests
import json

url = "https://gorest.co.in/public/v2/users/12"
data = requests.get(url)
print(data.text)
jsonOb = json.loads(data)
jsonS = json.dumps(jsonOb)
print(data.text['name'])

postUrl = "https://gorest.co.in/public/v2/users"
myData = {
    "id":12,
    "name":"Jyoti Dhawan DDS",
    "email":"jyoti_dhawan_dds@green.info",
    "gender":"male",
    "status":"active"
}

token = '6c97c78691234a5a80b2f0f7b4b8f1cffca54f23b71d7cf07f600bd654c078c4'	
header = {
    "Authorization": f"Bearer {token}"
}
resp = requests.post(postUrl, myData, header)