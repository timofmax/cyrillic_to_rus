
from transliterate import translit, get_available_language_codes
from mp3_tagger import *
from glob import glob
import os


sps = os.listdir()
[os.rename(i, translit(i, 'ru', reversed=True)) for i in sps]
sps = os.listdir()
new = []
[new.append(i) for i in sps if "mp3" in i]

sps = new
try:
    for i in sps:
        print(i)
        mp3 = MP3File(i)
        mp3.set_version(VERSION_BOTH)
        mp3.song = i.encode("utf-8").decode("latin-1")
        mp3.save()
        print("{} writed".format(i))
except MP3OpenFileError:
    print("{} not a .mp3".format(i))

