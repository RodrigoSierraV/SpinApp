from requests import get
from sys import exit

token = 'BQCv2EqlZoCdBvxyQ4u_KDyvg9vUeQ1Y8o0ld0TVue_ZbjEu5mWK2eBz6RTXEsKjVr80jr97Lx3OjbTwApK_0MS7z2FSeM7dIPKrTkQKHqCaCp33XGJDDR5Qpjyn3xjM011N6Ze9iU45EdRLbvslt4lBQgAaRso_Ea8HOIROXw9XzESMNmYok8QaXqUkOXE2UFqnTqg-Vrai2zrHTOCtCTRHqQquYF_pPw'

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
        print('No artist')

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
                print("{};{};{}".format(name, key, energy_dict[key]))

