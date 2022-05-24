import json
import re
import random
import requests
from secrets import playlist_total_token, playlist_items_token

      
# function for pretty printing JSON data, creates formatted string of JSON object
def jprint(self, obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    return text
    
    
# recieves class attributes and extracts playlist IDs from URLs
def recieve_playlist_ids(self):
    
    # removes protocols and other parts of URL not matching an alphanumeric playlist ID i.e "37i9dQZF1DWT6MhXz0jw61"
    pattern = re.compile('^https://open.spotify.com/playlist/([a-zA-Z0-9]+).*$')

    
    playlists = ["https://open.spotify.com/playlist/37i9dQZF1DWT6MhXz0jw61?si=c6c62f9348044ab0", 
                "https://open.spotify.com/playlist/37i9dQZF1DWYmmr74INQlb?si=17c3bf40339e4a4a", 
                "https://open.spotify.com/playlist/0L3CyZ90B6csQ50jb0idrL?si=43c1a6b3bc604182", 
                "https://open.spotify.com/playlist/37i9dQZF1EUMDoJuT8yJsl?si=7665e943ff994818", 
                "https://open.spotify.com/playlist/58NUu1xNbb0AGiovGV0Sl8?si=86b47f62f3e64094"
                ]


    # uses regular expression to match playlist links and extract playlist ID from URL
    playlist_ids = [pattern.findall(play_id)[0] for play_id in playlists]
    return playlist_ids 


# recieves total number of tracks from "Get_Playlist" endpoint
def get_playlist_total(self):
    playlist = f"https://api.spotify.com/v1/playlists/58NUu1xNbb0AGiovGV0Sl8"
    
    response = requests.get(
        playlist , # API endpoint
        
        headers={
            "Authorization": f"Bearer {playlist_total_token}"
        },
        params={
            "fields": "tracks.total"
            }
    )
        
    
    json_data = dict(response.json())['tracks']['total']
    return json_data


# uses playlist IDs to call Spotify Web API and save JSON response data
def extract_playlist_json(self):
    
    pid1, pid2, pid3, pid4, pid5 = recieve_playlist_ids()
    
    p1 = f"https://api.spotify.com/v1/playlists/{pid1}/tracks" 
    p2 = f"https://api.spotify.com/v1/playlists/{pid2}/tracks"
    p3 = f"https://api.spotify.com/v1/playlists/{pid3}/tracks"
    p4 = f"https://api.spotify.com/v1/playlists/{pid4}/tracks"
    p5 = f"https://api.spotify.com/v1/playlists/{pid5}/tracks"
    playlist_total = get_playlist_total()
        
        
        
    # API response specifications
    fields = "items(track(name,href,total))"
    random_offset = 0
    used_offset = []
    
    # Randomise offset to retrieve different results in different API calls
    
    if playlist_total > 50 and random_offset not in used_offset:
        random_offset = random.randrange(playlist_total//50) * 50
        used_offset.append(random_offset)
    
    print(random_offset)

    # GET request for playlist
    response = requests.get(
        p5, # API endpoint
        headers={
            "Authorization": f"Bearer {playlist_items_token}"
        },
        params={
            "fields": fields,
            "limit" : 2,
            "offset" : random_offset
            }
    )

    json_data = Roulette.jprint(response.json())
    
    # dumps prettified JSON data to data.json for later parsing
    with open('data.json', 'w') as f:
        json.dump(response.json(), f, indent=4)
    
    return json_data


