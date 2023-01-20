import requests

# Set the request parameters
url = 'https://dev139371.service-now.com/api/now/table/incident'

# Set proper headers
headers = {"Content-Type": "application/json", "Accept": "application/json",
           "Authorization": "Bearer QPfFPnRNhkxqN-bAQLAhQ6bykv9_LxgGrlDFOY_LhRYodj4IeeDevKppVtZ_2gYrTbX9p9WsknE_Y5W7qDlVTQ"}

# Do the HTTP request
response = requests.get(url, headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
