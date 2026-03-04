import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/packetcaptures"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "id": 0,
  "start_time": "2026-02-10T17:23:24.625Z",
  "end_time": "2026-02-10T17:23:24.625Z",
  "org_id": 0,
  "name": "string",
  "duration": 604800,
  "capture_id_type": "AP_SERIAL_NUMBER",
  "ap_serial_number": "string",
  "device_ids": [
    0
  ],
  "location_id": 0,
  "destination": "CLOUD",
  "filter": {
    "mac_addr": [
      "string"
    ],
    "ip_addr": [
      "string"
    ],
    "protocol": "ANY",
    "protocol_number": 255,
    "port": 0,
    "vlan": "string",
    "wlan": "string"
  },
  "capture_if": {
    "direction": "BOTH",
    "radio": "ALL",
    "wired_interface": "ALL",
    "wireless_band": "ALL",
    "wired_filters": [
      "DHCP"
    ],
    "wireless_filters": [
      "MANAGEMENT"
    ]
  },
  "status": "INITIAL",
  "results": [
    {
      "id": 0,
      "org_id": 0,
      "start_time": "2026-02-10T17:23:24.625Z",
      "end_time": "2026-02-10T17:23:24.625Z",
      "device_id": 0,
      "hostname": "string",
      "mac_address": "string",
      "interface_name": "string",
      "location_id": 0,
      "locations": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "INITIAL",
      "error_message": "string",
      "storage": {
        "cloud_storage": "string",
        "cloud_shark_storage": {
          "file_name": "string",
          "file_url": "string"
        }
      }
    }
  ],
  "cloud_storage": "string"
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
