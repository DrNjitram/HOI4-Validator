from codecs import open
from os import listdir
import os
import json

path = "D:\SteamLibrary\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels"

with open(os.path.join(path, "songnames.txt"), 'w', 'utf-8') as outputfile:
    outputfile.truncate()
    for file in listdir(path):
        if "songnames" not in file:
            for file_ in listdir(os.path.join(path, file)):
                if "info.dat" == file_:
                    lines = open(os.path.join(path, file, file_), 'r', 'utf-8')
                    json_data = json.load(lines)
                    outputfile.write(json_data["_songName"].strip() + "\n")
