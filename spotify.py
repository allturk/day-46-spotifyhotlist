import json
import os
import spotipy
from spotipy import SpotifyOAuth

PLAYLIST = {
    "name": "Time Machine Hot-100",
    "description": "Time Machine Billboard Hot-100 playlist",
    "public": False,
}
REDIRECT_URL = "https://www.example.com"
TOKEN = "token.txt"
SCOPE_MODIFY = "playlist-modify-private"
SCOPE_READ = "playlist-read-private"
PLAYLIST_ID=os.getenv("PlIST_ID")


class SpotifyProcess:
    singer_and_songs = {}
    def __init__(self):
        self.client_id = os.getenv("SPFY-CLI-ID")
        # self.client_id =""
        self.client_sec = os.getenv("SPFY-CLI-SEC")
        # self.client_sec=""
        self.user_id = "1"
        self.playlist_id = PLAYLIST_ID
        self.song_uris = []
        self.songs_found={}
        self.date=""

    def connect_spotify(self, scope):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                       client_secret=self.client_sec,
                                                       redirect_uri=REDIRECT_URL,
                                                       cache_path=TOKEN,
                                                       scope=scope,
                                                       show_dialog=True,
                                                       ))
        return sp

    def create_playlist(self):
        sp = self.connect_spotify(SCOPE_MODIFY)
        playlist_name = input("Pleas enter your playlist name which is going to be created: ")
        self.user_id = sp.current_user()["id"]
        try:
            self.playlist_id = sp.user_playlist_create(user=self.user_id, name=playlist_name, public=False)
        except:
            print(f"An Error occurred while creating your playlist {playlist_name}")
        else:
            print("Your playlist created")

    def get_song_uri(self):

        sp = self.connect_spotify(SCOPE_MODIFY)
        self.songs_found=self.singer_and_songs.copy()
        for song in self.singer_and_songs.items():
            result = sp.search(f"{song[0]} {song[1]}")
            # pprint(result)
            try:
                uri = result["tracks"]["items"][0]["uri"]
                self.song_uris.append(uri)
            except IndexError:
                self.songs_found.pop(song[0])

                # print(f"{song[1]} doesn't exist in Spotify. Skipped.")

    def write_to_file(self):
        try:
            with open(f"spotify_uris{self.date}.json", "w") as file:
                json.dump(self.song_uris, file, indent=4)
        except:
            print("An error occurred while writing uri file")
        else:
            print(f"spotify_uris{self.date}.json file was successfuly created")

    def read_present_file(self):
        file_name = input("Pleas enter a file name which has your song uri list (file.json): ")
        with open(file_name, "r") as file:
            self.song_uris = json.load(file)

    def add_tracks(self):
        # self.get_playlist_id()
        sp = self.connect_spotify(SCOPE_MODIFY)
        sp.user_playlist_add_tracks(user=sp.current_user()["id"], playlist_id=self.playlist_id, tracks=self.song_uris)

    def get_playlist_id(self):
        with open("palylistid.txt", "r") as file:
            self.playlist_id = file.read()

    def remove_tracks(self):
        self.get_playlist_id()
        sp=self.connect_spotify(SCOPE_MODIFY)
        sp.user_playlist_remove_all_occurrences_of_tracks(user=sp.current_user()["id"],playlist_id=self.playlist_id,tracks=self.song_uris)