from requests import get
from sys import exit
import urllib.request
import urllib.parse
import re

token = 'BQCpkpXcdgkxF43fpLJPLzTuj0Jmtx5taIWU0mgqT2pWIU31ao_e4ngQN53VcG9tMkQ_3YdunlcsNVKZxtpFTuIG063wfLXCm3bp0VswMfqE6-hGrHawTgvBYtCno2C9fa_YE1rVtYiRaKfalfqvlVQzbkglD75qIknGnoom9ptkr9Ovjl4OP_m81BfqQgJy-V7VMMv24vm9ggglaKO_U27HwpWEJ5_PVg'

file = 'artists_list.txt'
list_of_artists = []
with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        list_of_artists.append(line[:-1])

#print('Enter energy level (0 - 100):')
#energy_level = int(input())/100

energy_level = 1/100

for name in list_of_artists:

    id_artist = get("https://api.spotify.com/v1/search?q={}&type=artist".format(name), headers={"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer {}".format(token)})

    try:
        artist_id = id_artist.json()['artists']['items'][0]['id']
    except:
        continue 

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
        try:
            energy_list.append(key['energy'])
            energy_dict[ids_dict[key['id']]] = key['energy']
        except:
            pass

    if len(energy_list) > 0:
        if energy_level > max(sorted(energy_list, reverse=True)):
            continue
        for key in energy_dict:
            if energy_dict[key] >= energy_level:
                query_string = urllib.parse.urlencode({"search_query" : "{} {}".format(name, key)})
                html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                print("{};{};{};{}".format(name, key, energy_dict[key], search_results[0]))


