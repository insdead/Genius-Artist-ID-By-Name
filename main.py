import requests, json

url = "https://api.genius.com"
CLIENT_ACCESS_TOKEN = "cXeSZvtkGqZw2BQ5U0azVqCgslsJ49NikZ1VKnIpq4prp3TcOc8DnhCFV2vHDyA5"
name = input('Write the name ')

def _get(path, params=None, headers=None):

    requrl = '/'.join([url, path])
    token = "Bearer {}".format(CLIENT_ACCESS_TOKEN)
    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    response = requests.get(url=requrl, params=params, headers=headers)
    response.raise_for_status()

    return response.json()

print("searching " + name + "'s artist id. \n")

find_id = _get("search", {'q': name})
for hit in find_id["response"]["hits"]:
   if hit["result"]["primary_artist"]["name"] == name:
       artist_id = hit["result"]["primary_artist"]["id"]
       break

print("-> " + name + "'s id is " + str(artist_id) + "\n")
