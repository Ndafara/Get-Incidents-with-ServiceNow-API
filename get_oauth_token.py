import requests

# Set the request parameters
url = 'https://dev139371.service-now.com/oauth_token.do'

# Set proper headers
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# Set the urlencoded body
username = 'aes.creator'
password = '9sv0NRT-Euk@'
grant_type = 'password'
client_id = 'fbd8685975982110a2713f7fdf73d3b9'
client_secret = 'Wd@.O`Ru[X'

data = {'username': username, 'password': password, 'grant_type': grant_type,
        'client_id': client_id, 'client_secret': client_secret}

# Do the HTTP request
response = requests.post(url, headers=headers, data=data)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
