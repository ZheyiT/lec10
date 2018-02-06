
from requests_oauthlib import OAuth1Session
import secrets
import json
import requests

client_key = secrets.client_key
client_secret = secrets.client_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
#r = requests.get(protected_url, params=params)

r_dict = json.loads(r.text)


#print(r_dict["user"]["name"])
for i in r_dict["statuses"]:
	print(i["user"]["name"])
	print(i["text"])
	print("--------------------")

