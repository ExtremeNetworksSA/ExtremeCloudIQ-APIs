import requests
         
baseUrl = 'https://api.extremecloudiq.com'
parent_id = 'Parent ID'
floor_id = 'Floor ID '
client_mac = 'Client MAC address'
access_token = '***'

url = f"{baseUrl}/essentials/eloc/clients/location/path-in-interval-on-floor"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'parentId': f'{parent_id}', 'floorId': f'{floor_id}', 'clientMac': f'{client_mac}', 'startDate': '2026-01-01 00:00', 'endDate': '2026-01-01 23:59'}



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
