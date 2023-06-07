# -*- coding: utf-8 -*-
"""
Created on 2023/4/4
Edited on 2023/4/17
Changed on 2023/6/5
@author: soburi
"""
import sys, subprocess
import re

while(True):
    path = input("(Default:[Enter] →~/Music/Music)\nTarget path:") or "~/Music/Music"

    if (path == "end"):
        break

    url = input("(play list url ok)\n(Default:[Enter]→import music.txt)\nmovie url:")
    cmd = f".\yt-dlp\yt-dlp.exe --ffmpeg-location ./ffmpeg/ffmpeg.exe --parse-metadata artist:%(channel)s -o {path:s}/%(title)s -f b --add-metadata --extract-audio --embed-thumbnail --audio-format mp3 "
    
    list = []
    if re.match("https?://[\w!\?/\+\-_~=;\.,\*&@#\$%\(\)'\[\]]+", url):
        tmp = url
        if "list=" in url:
            if re.match('http(s)?:\/\/(www.youtube.com\/|youtu.be\/)', url):
                tmp = "https://youtube.com/playlist?list="+re.findall(r"(?:list=|\/)([0-9A-Za-z_-]{34}).*", url)[0]
                url = tmp
            end = int(input("(example:3→download the 3 lastest music)\n(Default:[Enter]→download all)\n end num:") or 0)
            if end != 0:
                tmp = f"--playlist-end {end} --yes-playlist {url}"
        list.append(tmp)

    else:
        try:
            with open(url, mode='r') as f:
                list = f.readlines()
        except:
            print("nothing text file.")
            sys.exit(1)
    
    for urls in list:
        subprocess.run('echo '+cmd+urls, shell=True)
        subprocess.run(cmd+urls, shell=True) 
