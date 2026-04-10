import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv("OKTA_TOKEN")
domain = os.getenv("OKTA_DOMAIN")

url = f"{domain}/api/v1/users"

headers = {
    'Authorization': f"SSWS {api_token}",
    'Content-Type': 'application/json'
}

response = requests.get(url,headers=headers, verify=False)

print(response.status_code)
res = response.json()
for user in res:
    print(user['profile']['firstName']+' '+user['profile']['lastName'] +'|'+ user['profile']['email'])