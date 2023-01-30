#Create an U.I for this with GUI!

import os
from tkinter import Menu
from pytube import YouTube, Playlist, Search
#from

def menu():
    Type = input("[1] Single video\n[2] playlist\n[3] Search\n[0] exit\n: ")

    if Type == "1":
        SVid()
    if Type == "2":
        PlayList()
    if Type == "3":
        YtSearch()
    if Type == "0":
        exit()    
    else:
        menu()

def SVid():
    SLink = input("What is the videos link? ")
    yt = YouTube(SLink)
    print("Tile : ", yt.title)
    yd = yt.streams.get_highest_resolution()
    yd.download("D:\General\Programming\python\Projects\Automation\Youtube Vid Downloader\Downloades\SingleVid")
    print("Downloaded!\n")

def PlayList():
    PLink = input("What is the playlist's link? ")
    P = Playlist(PLink)
    global PName
    OriginalPName = P.title
    print(OriginalPName)
    OriginalPName = CreateFolder(OriginalPName)
    for video in P.videos:
        print("---------------------------------------------------")
        print(video.title)
        Pd = video.streams.get_highest_resolution()
        
        Pd.download(f"D:\General\Programming\python\Projects\Automation\Youtube Vid Downloader\Downloades\Playlist\{OriginalPName}")
        print(video.title, "Downloaded!")
        print("---------------------------------------------------")


def YtSearch():
    SName =  input("Name of the video? ")
    S = Search(SName)
    S = S.results[0]
    print("Tile : ", S.title)
    Sd = S.streams.get_highest_resolution()
    Sd.download("D:\General\Programming\python\Projects\Automation\Youtube Vid Downloader\Downloades\Search")
    print("Downloaded!\n")
    option = input("Would you like to search again> (Y/N) ").lower()
    if option == "y":
        YtSearch()

def CreateFolder(OriginalPName):
    os.chdir("D:\General\Programming\python\Projects\Automation\Youtube Vid Downloader\Downloades\Playlist")
    Existing = FileChecker(OriginalPName)
    if Existing == True:
        num = 0
        while Existing == True:
            num = num + 1
            PName = (OriginalPName + "(" + str(num) + ")")
            Existing = FileChecker(PName)
            if Existing == False:
                print("New folder was made called:", PName)
                os.mkdir(PName)
                return PName
    return OriginalPName

def FileChecker(PName):
    if not os.path.exists(f"D:\General\Programming\python\Projects\Automation\Youtube Vid Downloader\Downloades\Playlist\{PName}"):
        Existing = False
    if os.path.exists(f"D:\General\Programming\python\Projects\Automation\Youtube Vid Downloader\Downloades\Playlist\{PName}"):
        Existing = True
    return Existing

menu()
