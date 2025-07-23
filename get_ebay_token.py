import requests
import base64

# Replace with real eBay app credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

auth_string = f"{client_id}:{client_secret}"
b64_auth = base64.b64encode(auth_string.encode()).decode()

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Basic {b64_auth}'
}

data = {
    'grant_type': 'client_credentials',
    'scope': 'https://api.ebay.com/oauth/api_scope'
}

response = requests.post(
    'https://api.ebay.com/identity/v1/oauth2/token',
    headers=headers,
    data=data
)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())
