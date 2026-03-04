import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/locations/folder/zones"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "folder_id": 4004,
  "zones": [
    {
      "color": "string",
      "coordinates": [
        {
          "x": 3069.3426257470537,
          "y": 1662.227928411435
        },
        {
          "x": 6525.310861208309,
          "y": 1526.1548831038363
        }
      ],
      "id": 9301,
      "name": "string",
      "visible": True,
      "zone_vertical_align": "TOP"
    },
    {
      "color": "string",
      "coordinates": [
        {
          "x": 8158.27311757249,
          "y": 3234.373490369098
        },
        {
          "x": 5526.855869489531,
          "y": 5589.372283801082
        }
      ],
      "id": 5080,
      "name": "string",
      "visible": False,
      "zone_vertical_align": "BOTTOM"
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
