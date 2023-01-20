import requests

# Set the request parameters
url = 'https://dev139371.service-now.com/api/now/table/incident'

# Set the user and password credentials
user = 'aes.creator'
password = '9sv0NRT-Euk@'

# Set proper headers
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, password), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
