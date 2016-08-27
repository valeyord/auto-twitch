# Author: Rodrigo 'valeyord' Lima
# This script opens a twitch channel in popout video and popout chat window-size
# Version 0.2
# -*- coding: utf-8 -*-
from subprocess import Popen, call
PATH ="/home/rodrigo/python/myScripts/auto-twitch/"
def mainMenu():
    call(["clear"], shell=True)
    with open("/home/rodrigo/python/myScripts/auto-twitch/savedChannels.txt", "r+") as savedChannels:
        print(savedChannels.read())
    print("Type 'add channel' to add a new channel to the list")
    channel = raw_input("\nType a Twitch Channel: ")
    if channel[:4] == "add ":
        AddChannel(channel[4:])
    else:
        OpenTwitch(channel)

def AddChannel(x):
    with open("/home/rodrigo/python/myScripts/auto-twitch/savedChannels.txt", "a") as savedChannels:
        savedChannels.write(x + "\n")
    mainMenu()
# Call google-chrome windows from terminal
def OpenTwitch(y):
    Popen(["google-chrome \
    --user-data-dir='{}chrome-video-data' \
    --new-window --window-position=0,0 --window-size=990,768 \
    --app='https://player.twitch.tv/?volume=0.5&channel={}'".format(PATH, y)], shell=True)
    Popen(["google-chrome \
    --user-data-dir='{}chrome-chat-data' \
    --new-window --window-position=1000,0 --window-size=366,768 \
    --app='https://www.twitch.tv/{}/chat?popout='".format(PATH, y)],shell=True)

mainMenu()
