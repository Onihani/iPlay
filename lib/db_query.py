#Importing libraries
import sqlite3
import re

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("database.db", check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS songs(song_title)"
        )
        self.conn.commit()

    def get_songs(self):
        songs = []
        self.cur.execute(
            "SELECT * FROM songs"
        )
        res = self.cur.fetchall()
        for i in res:
            songs.append(i[0])
        return songs

    def get_matched_songs(self, song_name):
        self.song_name = song_name.split()
        self.matched_songs = []
        db_songs = self.get_songs()
        for song in db_songs:  
            cur_song = re.sub(r"[,@\'?\.$%_]", "", song, flags=re.I)  
            for reg in self.song_name:
                if reg in cur_song:
                    self.matched_songs.append(song)
        return self.matched_songs
        

    def insert_song(self, song_title):
        self.cur.execute(
            "INSERT INTO songs VALUES('{}')".format(song_title)
        )
        self.conn.commit()
        
db = Database()
#print(db.get_songs())
#db.get_matched_songs("hindu")
#db.insert_song("hindu_baba_mole_.mp3")