# Author: Rodrigo 'valeyord' Lima
# This script opens a twitch channel in popout video and popout chat window-size
# Version 0.2
# -*- coding: utf-8 -*-
from subprocess import Popen, call
# Clear terminal
call(["clear"], shell=True)
# Save path location to store chrome-data directories (one-time/prototype)
PATH = "/home/rodrigo/python/myScripts/auto-twitch/"
# Print saved channels (prototype)
print("""My Saved Channels:
    -amazhs
    -trumpsc
    """)
# Read the channel to open
channel = raw_input("\nType a Twitch Channel: ")
# Call google-chrome windows from terminal
Popen(["google-chrome \
--user-data-dir='{}chrome-video-data' \
--new-window --window-position=0,0 --window-size=990,768 \
--app='https://player.twitch.tv/?volume=0.5&channel={}'".format(PATH, channel)], shell=True)
Popen(["google-chrome \
--user-data-dir='{}chrome-chat-data' \
--new-window --window-position=1000,0 --window-size=366,768 \
--app='https://www.twitch.tv/{}/chat?popout='".format(PATH, channel)],shell=True)
