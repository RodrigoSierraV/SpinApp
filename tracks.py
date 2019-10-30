from requests import get

token = 'BQBr-Achh5o9Qx06fDk05nndefLPdusw_N_mjp3n3GKcOBqvTE8gfV38ylxGVogs4hlvpe3x9Mwe1zncgwJz6P3kxw5GX1VDCiPssuGHBO2z4KgMGja8LztrWYiX0D6rRu7nHzDELsMl5fE99sWqFjv2g4UM4lh54wpZWsYXUSrY8YO7Ilvtw6RpKw4-3b_T5UoM35AzUNvVZs1bhrsAT_9hlZNLsIMzqA'

id_artist = get("https://api.spotify.com/v1/search?q=avicii&type=artist", headers={"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer {}".format(token)})

artist_id = id_artist.json()['artists']['items'][0]['id']

response = get("https://api.spotify.com/v1/artists/{}/top-tracks?country=us".format(artist_id), headers={"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer {}".format(token)})
ids_list = []
ids_dict = {}
dict_values = response.json().values()
vlst = list(dict_values)
for key in vlst[0]:
    ids_list.append(key['id'])
    ids_dict[key['id']] = key['name']

response2 = get("https://api.spotify.com/v1/audio-features?ids="+('%2C').join(ids_list), headers={"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer {}".format(token)})
energy_dict = {}
energy_list = []
for key in list(response2.json().values())[0]:
    energy_list.append(key['energy'])
    energy_dict[ids_dict[key['id']]] = key['energy'] 
print(energy_dict)
