import requests

response = requests.get(
    "https://www.eventbriteapi.com/v3/users/me/owned_events/",
    headers = {
        "Authorization": "Bearer R3PE2OGPQEXNYJYY6B2G",
    },
    verify = True,  # Verify SSL certificate
)
print (response.json()['events'][0]['name']['text'])

