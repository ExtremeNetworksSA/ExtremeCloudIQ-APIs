import requests
         
floorId = '8267'
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/locations/floor/{floorId}/walls"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "walls": [
    {
      "type_id": 9457,
      "x1": 7255.029545445447,
      "x2": 6435.344006079665,
      "y1": 1695.621669519367,
      "y2": 6909.798272451648,
      "close": 7935,
      "closed": False
    },
    {
      "type_id": 8525,
      "x1": 8063.995114028888,
      "x2": 6391.977576740296,
      "y1": 9180.186253851572,
      "y2": 8139.961808725981,
      "close": 4411,
      "closed": False
    }
  ]
}


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
