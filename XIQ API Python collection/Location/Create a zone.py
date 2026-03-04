import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/locations/folder/zones"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "color": "string",
  "coordinates": [
    {
      "x": 9277.69028270732,
      "y": 1531.7758327851404
    },
    {
      "x": 2262.6394749187084,
      "y": 2384.3017933629085
    }
  ],
  "folder_id": 7050,
  "name": "string",
  "zone_vertical_align": "BOTTOM",
  "visible": True
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
