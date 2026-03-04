import requests
         
reportScheduleId = '4987'
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/ng-reports/scheduled/custom/{reportScheduleId}/runs"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'frequency': 'WEEKLY'}



response = requests.get(url, headers=headers, params=params)

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
