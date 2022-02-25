import json
import requests
from secrets import spotify_id, spotify_token


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def retrieve_playlist():
    
    playlist_id = "58NUu1xNbb0AGiovGV0Sl8"
    
    playlist = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"    # playlist url
    fields = "items(track(name,href,artists(name),album(name)))"

    response = requests.get(
        playlist,
        headers={
            "Authorization": f"Bearer {spotify_token}"
        },
        params={
            "fields": fields
            }
    )

    json_data = jprint(response.json())
    return json_data


retrieve_playlist()