import requests
         
reportId = '4987'
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/ng-reports/scheduled/custom/{reportId}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "file_format": [
    "PDF",
    "XLSX"
  ],
  "metrics": [
    "UNIQUE_CLIENTS_BY_SSID",
    "CLIENT_AIRTIME_USAGE"
  ],
  "recipients": [
    {
      "email": "string",
      "notifier_id": 2821
    },
    {
      "email": "string",
      "notifier_id": 7836
    }
  ],
  "report_name": "string",
  "schedules": [
    {
      "frequency_type": "DAILY",
      "schedule_time": "string",
      "schedule_timezone": "string",
      "schedule_days": [
        2324,
        8613
      ],
      "enable_schedule": True
    },
    {
      "frequency_type": "DAILY",
      "schedule_time": "string",
      "schedule_timezone": "string",
      "schedule_days": [
        3285,
        7783
      ],
      "enable_schedule": False
    }
  ],
  "report_description": "string",
  "site_ids": [
    7408,
    5933
  ],
  "building_ids": [
    5952,
    7435
  ],
  "floor_ids": [
    2541,
    3852
  ],
  "ssids": [
    "string",
    "string"
  ],
  "bands": [
    "TWO_GHZ",
    "SIX_GHZ"
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
