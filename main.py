import os
from dotenv import load_dotenv
from requests import post
import requests
import base64
import json 

load_dotenv() 

client_id = os.getenv("CLIENT_ID1")
client_secret = os.getenv("CLIENT_SECRET1")

#authentication to base64
string = client_id + ':' + client_secret
string_bytes = string.encode('ascii') 
base64_bytes = base64.b64encode(string_bytes)
base64_string = base64_bytes.decode('ascii')

#Token
url = 'https://accounts.spotify.com/api/token'
 
headers = {'Authorization': f'Basic {base64_string}',
           'Content-Type': 'application/x-www-form-urlencoded'}

data = {'grant_type': 'client_credentials'} #body é o dicionario
response = requests.request('POST', url = url, headers = headers, data = data)
token = response.json()["access_token"]
print(token)

____________________________________________________________________________
#request search for an artists 
def search_for_artist(token, artist_name):
  url ="http://api.spotify.com/v1/search"
  headers = {'Authorization':f'Bearer {token}'}
  query = f"?q={artist_name}&type=artist&limit=1"

  query_url = url + query
  response = requests.request('GET', query_url, headers=headers)
  json_result = json.loads(response.content)["artists"]["items"]
  return json_result

#get you 10 top tracks
def get_toptracksong(token, artist_id): 
  url = f"http://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=BR"
  headers = {'Authorization':f'Bearer {token}'}
  response= requests.request('GET', url, headers=headers)
  json_result = json.loads(response.content)["tracks"]
  return json_result

token = ''
search_for_artist(token, "")
artist_id = ""
songs = get_toptracksong(token,artist_id)

for idx, song in enumerate(songs):
  print(f"{idx + 1}. {song['name']}")

