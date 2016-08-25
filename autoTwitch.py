# -*- coding: utf-8 -*-
from subprocess import call
call(["google-chrome --window-position=0,0 --window-size=1000,766 \
 --app='https://www.twitch.tv' & google-chrome --new-window --window-position=1000,1000\
 --app='https://www.google.com'"], shell=True)
