#Author: Rodrigo 'valeyord' Lima
#This script opens a twitch channel in popout video and popout chat window-size
#Version 0.2
# -*- coding: utf-8 -*-
from subprocess import Popen, call
call(["clear"], shell=True)
print("""Type a channel or pick one above:
    1)amazhs
    2)trumpsc
    """)
channel = raw_input("\n")
if channel == 1:
    channel = amazhs
elif channel == 2:
    channel = trumpsc
Popen(["google-chrome \
--user-data-dir='/home/rodrigo/python/myScripts/auto-twitch/chrome-video-data' \
--new-window --window-position=0,0 --window-size=990,768 \
--app='https://player.twitch.tv/?volume=0.5&channel={}'".format(channel)], shell=True)
Popen(["google-chrome \
--user-data-dir='/home/rodrigo/python/myScripts/auto-twitch/chrome-chat-data' \
--new-window --window-position=1000,0 --window-size=366,768 \
--app='https://www.twitch.tv/{}/chat?popout='".format(channel)],shell=True)
