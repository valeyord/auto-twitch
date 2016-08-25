# -*- coding: utf-8 -*-
from subprocess import Popen
Popen(["google-chrome \
--user-data-dir='/home/rodrigo/python/myScripts/auto-twitch/chrome-video-data' \
--new-window --window-position=0,0 --window-size=990,768 \
--app='https://www.google.com'"], shell=True)
Popen(["google-chrome \
--user-data-dir='/home/rodrigo/python/myScripts/auto-twitch/chrome-chat-data' \
--new-window --window-position=1000,0 --window-size=366,768 \
--app='https://www.twitch.tv'"],shell=True)
