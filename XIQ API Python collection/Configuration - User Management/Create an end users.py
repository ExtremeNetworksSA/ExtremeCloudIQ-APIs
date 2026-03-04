import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/endusers"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "user_group_id": 0,
  "name": "string",
  "user_name": "string",
  "organization": "string",
  "visit_purpose": "string",
  "description": "string",
  "email_address": "string",
  "phone_number": "string",
  "password": "string",
  "email_password_delivery": "string",
  "sms_password_delivery": "string"//,
  //"vlan_override": 4094 //description	:	VLAN ID override assigned to the user (range 1-4094, Optional)

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
