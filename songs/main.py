from mp3_tagger import MP3File

mp3 = MP3File("song1.mp3")

tags = mp3.get_tags()
print(tags)