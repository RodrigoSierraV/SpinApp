from requests import get
from sys import exit

token = 'BQBzHPfZksx8p-7aKudGsnBS4ccmYenMlz8Yf1oLE9d1ChoVdpIYygOBn5CQoBcd9tjuY7fijyGkrX7A1CQ_at_cZC__5meTYCSiOTRLO17y5pI-eFqBYwTFL_qpfAYapERUFt1knpztp94FiIurJ0FyhXi4KiqFUYSJAp_00uQq7ObyHud_52ivB0X8vugvdJZTJvtygF4DousYcssFlFgol7AfbKA9Vw'

print('Enter artist name:')
name_artist = input()

id_artist = get("https://api.spotify.com/v1/search?q={}&type=artist".format(name_artist), headers={"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer {}".format(token)})

try:
    artist_id = id_artist.json()['artists']['items'][0]['id']
except:
    print('No artist')
    exit(0)

print('Enter energy level (0 - 100):')
energy_level = int(input())/100

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

if energy_level > max(sorted(energy_list, reverse=True)):
    print('There are no songs with that level')
    exit(0)
for key in energy_dict:
    if energy_dict[key] >= energy_level:
        print(key, ':', energy_dict[key])

