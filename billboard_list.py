import requests
from bs4 import BeautifulSoup as bs4
import json
from spotify import SpotifyProcess
import lxml

HOT_100_URL = "https://www.billboard.com/charts/hot-100/"
TAGS = "li h3"
TAG_CLASS = "title-of-a-story"
SEARCH_TAG_NAME = "span"
SEARCH_TAG_CLASS = "c-label"
STRIP_TEXT = "\t\n1234567890"

class Billboard(SpotifyProcess):

    def __init__(self):
        super().__init__()
        self.url = HOT_100_URL
        self.tags = TAGS
        self.tag_class = TAG_CLASS
        self.search_tag_name = SEARCH_TAG_NAME
        self.search_tag_class = SEARCH_TAG_CLASS
        self.strip_text = STRIP_TEXT
        self.singer_names = []
        self.song_names = []
        self.song_and_singer={}
        self.list_date=""

    def connect_billboard(self):
        # self.list_date = input("Which yer do you want to travel to? Type the date in this format YYYY-MM-DD:")
        self.date = self.list_date
        response = requests.get(f"{HOT_100_URL}{self.list_date}")
        # with open("songs.html", "w", encoding="utf-8") as file:
        #     file.write(response.text)
        soup = bs4(response.text, "lxml")
        return soup

    def search_hotlist(self):
        soup = self.connect_billboard()
        songs = soup.select(selector=TAGS, class_=TAG_CLASS)
        print(songs)
        song_name = [song.getText().strip("\n\t") for song in songs]

        for indeks in range(100):
            self.song_names.append(song_name[indeks])
        singers = soup.find_all(name=SEARCH_TAG_NAME, class_=SEARCH_TAG_CLASS)
        singer_name = [singer.getText().strip(STRIP_TEXT) for singer in singers]
        for _ in singer_name:
            if _ != "" and _ != "-" and _ != "NEW":
                self.singer_names.append(_)
        self.singer_and_songs = {self.singer_names[item]: self.song_names[item] for item in range(0, 100)}
        return self.singer_and_songs




    def write_to_file(self):
        file_name = input("Please enter file name your song list going to be stored: ")
        try:
            with open(f"{file_name}.json", "w") as file:
                json.dump(self.song_and_singer, file, indent=4)
        except:
            print("An error occurred when writing the file")
        else:
            print(f"Your song file {file_name}.json is created")

    def read_present_file(self):

        file_name = input("Pleas enter a file name which has your song list (file.json): ")
        with open(file_name, "r") as file:
            self.song_and_singer = json.load(file)
