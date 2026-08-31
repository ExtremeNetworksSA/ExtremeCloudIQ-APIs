import requests
         
id_ = '8267'
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/tunnel-concentrators/{id_}/license/upload"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "data": "string",
  "file": "v10_license-2328V-EFAB6.xlc"
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
