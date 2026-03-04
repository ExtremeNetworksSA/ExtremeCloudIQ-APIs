import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/devices/thread/commissioner/stop"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "building_ids": [
    5761,
    1526
  ],
  "owner_id": 6396,
  "ext_pan_id": "1e11e11e11e11e11"
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
