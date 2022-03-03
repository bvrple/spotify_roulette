import json
import re
import random
import requests
from secrets import spotify_id, spotify_token


# must be provided with between 2-5 playlist links upon instantiation
class Roulette:
    def __init__(self, plist_one, plist_two, plist_three=None, plist_four=None, plist_five=None):
        
        # EACH CLASS ATTRIBUTE == PLAYLIST LINK i.e "https://open.spotify.com/playlist/37i9dQZF1DWT6MhXz0jw61?si=c6c62f9348044ab0
        self.plist_one = plist_one
        self.plist_two = plist_two
        self.plist_three = plist_three
        self.plist_four = plist_four
        self.plist_five = plist_five
        
        
    # writes playlist IDs to console when an instantiation of playlist class is printed
    def __str__(self):
        if self.plist_three == None:
            return f'PL1: {self.plist_one}\nPL2: {self.plist_two}'
        elif self.plist_four == None:
            return f'PL1: {self.plist_one}\nPL2: {self.plist_two}\nPL3: {self.plist_three}'
        elif self.plist_five == None:
            return f'PL1: {self.plist_one}\nPL2: {self.plist_two}\nPL2: {self.plist_three}\nPL3: {self.plist_four}'
        else:
            return f'PL1: {self.plist_one}\nPL2: {self.plist_two}\nPL3: {self.plist_three}\nPL4: {self.plist_four}\nPL5: {self.plist_five}'
            
            
    # function for pretty printing JSON data, creates formatted string of JSON object
    def jprint(obj):
    
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
        
        
    # recieves class attributes and extracts playlist IDs from URLs
    def recieve_playlist_ids(self):
        
        # removes protocols and other parts of URL not matching an alphanumeric playlist ID i.e "37i9dQZF1DWT6MhXz0jw61"
        pattern = re.compile('^https://open.spotify.com/playlist/([a-zA-Z0-9]+).*$')

        playlists = [
                    self.plist_one,
                    self.plist_two,
                    self.plist_three,
                    self.plist_four,
                    self.plist_five
                ]
        
        # playlists = ["https://open.spotify.com/playlist/37i9dQZF1DWT6MhXz0jw61?si=c6c62f9348044ab0", 
        #             "https://open.spotify.com/playlist/37i9dQZF1DWYmmr74INQlb?si=17c3bf40339e4a4a", 
        #             "https://open.spotify.com/playlist/0L3CyZ90B6csQ50jb0idrL?si=43c1a6b3bc604182", 
        #             "https://open.spotify.com/playlist/37i9dQZF1EUMDoJuT8yJsl?si=7665e943ff994818", 
        #             "https://open.spotify.com/playlist/58NUu1xNbb0AGiovGV0Sl8?si=86b47f62f3e64094"
        #             ]


        # uses regular expression to match playlist links and extract playlist ID from URL
        playlist_ids = [pattern.findall(play_id)[0] for play_id in playlists]
        return playlist_ids    


    # uses playlist IDs to call Spotify Web API and save JSON response data
    def extract_playlist_json(pid1, pid2, pid3=None, pid4=None, pid5=None)
        
        pid1, pid2, pid3, pid4, pid5 = Playlist.recieve_playlist_ids()
        
        p1 = f"https://api.spotify.com/v1/playlists/{pid1}/tracks" 
        p2 = f"https://api.spotify.com/v1/playlists/{pid2}/tracks"
        p3 = f"https://api.spotify.com/v1/playlists/{pid3}/tracks"
        p4 = f"https://api.spotify.com/v1/playlists/{pid4}/tracks"
        p5 = f"https://api.spotify.com/v1/playlists/{pid5}/tracks"
        
        # API response specifications
        fields = "items(track(name,href))"
        
        # random_offset = random.randrange(playlist_total)

        # GET request for playlist
        response = requests.get(
            p1 # API endpoint,
            headers={
                "Authorization": f"Bearer {spotify_token}"
            },
            params={
                "fields": fields,
                "limit" : 50,
                # "offset" : random_offset,
                # "total" : 4
                }
        )

        json_data = Roulette.jprint(response.json())
        
        # dumps prettified JSON data to data.json for later parsing
        with open('data.json', 'w') as f:
            json.dump(response.json(), f, indent=4)
        
        return json_data
    





play_print = Roulette(*["https://open.spotify.com/playlist/37i9dQZF1DWT6MhXz0jw61?si=c6c62f9348044ab0", 
                    "https://open.spotify.com/playlist/37i9dQZF1DWYmmr74INQlb?si=17c3bf40339e4a4a", 
                    "https://open.spotify.com/playlist/0L3CyZ90B6csQ50jb0idrL?si=43c1a6b3bc604182", 
                    "https://open.spotify.com/playlist/37i9dQZF1EUMDoJuT8yJsl?si=7665e943ff994818", 
                    "https://open.spotify.com/playlist/58NUu1xNbb0AGiovGV0Sl8?si=86b47f62f3e64094"
                    ])

print(play_print)