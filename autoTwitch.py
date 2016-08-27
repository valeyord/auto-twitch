# Author: Rodrigo 'valeyord' Lima
# This script opens a twitch channel in popout video and popout chat window-size
# Version 0.2
# -*- coding: utf-8 -*-
from subprocess import Popen, call
PATH ="/home/rodrigo/python/myScripts/auto-twitch/"
def mainMenu():
    call(["clear"], shell=True)
    print ("My saved channels:")
    with open("/home/rodrigo/python/myScripts/auto-twitch/savedChannels.txt", "r+") as savedChannels:
        print(savedChannels.read())
    print("Type 'add' before the channel to add it to the list")
    print("Type 'erase' before the channel to erase it from the list")
    print("Type 'erase all list' to clear the entire list")
    channel = raw_input("\nEnter a Twitch Channel: ")
    if channel[:4] == "add ":
        addChannel(channel[4:])
    if channel[:6] == "erase ":
        eraseChannel(channel[6:])
    else:
        openTwitch(channel)

def addChannel(x):
    with open("{}savedChannels.txt".format(PATH), "a") as savedChannels:
        savedChannels.write(x + "\n")
    mainMenu()
def eraseChannel(y):
    if y == "all list":
        Popen(["echo '' > {}savedChannels.txt".format(PATH)], shell=True)
        mainMenu()
    else:
        with open("{}savedChannels.txt".format(PATH), "r") as savedChannels:
            allChannels = savedChannels.readlines()
        with open("{}savedChannels.txt".format(PATH), "w") as savedChannels:
            for thisChannel in allChannels:
                if thisChannel != y + "\n":
                    savedChannels.write(thisChannel)
        mainMenu()
def openTwitch(z):
    Popen(["google-chrome \
    --user-data-dir='{}chrome-video-data' \
    --new-window --window-position=0,0 --window-size=990,768 \
    --app='https://player.twitch.tv/?volume=0.5&channel={}'".format(PATH, z)], shell=True)
    Popen(["google-chrome \
    --user-data-dir='{}chrome-chat-data' \
    --new-window --window-position=1000,0 --window-size=366,768 \
    --app='https://www.twitch.tv/{}/chat?popout='".format(PATH, z)],shell=True)

mainMenu()
