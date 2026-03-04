import requests
         
reportId = '4987'
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/ng-reports/scheduled/{reportId}/recipients"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = [
  {
    "email": "string",
    "notifier_id": 2974
  },
  {
    "email": "string",
    "notifier_id": 7436
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
