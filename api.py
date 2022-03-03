from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class PlaylistData(BaseModel):
    playlistNum: str
    href: str
    


class TrackData(BaseModel):
    track: str
    artist: str
    href: str
    
    

app.get("/")
def test_index():
    json_replica = {
        "playlists": {
            '0': 'https://open.spotify.com/playlist/37i9dQZF1DWT6MhXz0jw61?si=c6c62f9348044ab0', 
            '1': 'https://open.spotify.com/playlist/37i9dQZF1DWYmmr74INQlb?si=17c3bf40339e4a4a', 
            '2': 'https://open.spotify.com/playlist/0L3CyZ90B6csQ50jb0idrL?si=43c1a6b3bc604182', 
            '3': 'https://open.spotify.com/playlist/37i9dQZF1EUMDoJuT8yJsl?si=7665e943ff994818', 
            '4': 'https://open.spotify.com/playlist/58NUu1xNbb0AGiovGV0Sl8?si=86b47f62f3e64094'}
    }
    return json_replica