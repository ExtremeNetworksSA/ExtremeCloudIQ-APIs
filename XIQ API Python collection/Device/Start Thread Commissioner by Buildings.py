import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/devices/thread/commissioner/start"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "building_ids": [
    4265,
    7911
  ],
  "owner_id": 1330,
  "comm_timeout": 1621009,
  "ext_pan_id": "feD0B60A6efeD0B6"
}


response = requests.post(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
if content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
