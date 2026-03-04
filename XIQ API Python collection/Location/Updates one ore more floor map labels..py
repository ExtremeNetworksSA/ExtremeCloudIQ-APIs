import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/locations/floor/bulk/label"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = [
  {
    "id": 5927,
    "text": "string",
    "x": 9049.548834611458,
    "y": 9063.971998402072,
    "floor_id": 9534,
    "visible": False
  },
  {
    "id": 1720,
    "text": "string",
    "x": 3576.3344818964724,
    "y": 8594.292011583577,
    "floor_id": 7918,
    "visible": False
  }
]


response = requests.put(url, headers=headers, params=params)

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
