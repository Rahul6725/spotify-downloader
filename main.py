import os, re, logging
os.system('pip install spotdl')
from spotdl.command_line.core import Spotdl
from spotdl.authorize.services import AuthorizeSpotify
from spotdl.helpers.spotify import SpotifyHelpers
from spotdl.metadata_search import MetadataSearch
from spotdl import util, Spotdl


util.install_logger(logging.INFO)
os.system('cls')
liste = []
args = {}
file_name = "tracks.txt"


print('''

    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

        Welcome To Spotify Songs Downloader

    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

        Press 1). Download Track by url
        Press 2). Download Album by url
        Press 3). Download Playlist by url
        Press 4). Download Song by search
        Press 5). To display menu
        Press 6). Exit
                ''')

while(1):
    inp = int(input("Enter your choice: "))
    if inp == 1:
        print("You pressed 1!")
        print("Spotify track link should look like this: https://open.spotify.com/track/<gibberish-code>")
        url = str(input("Enter your song url: "))
        with Spotdl(args) as spotdl_handler:
            spotdl_handler.download_track(url)
        ch = str(input("Want to exit the program? Press[y/N]: "))
        if ch == 'y' or ch == 'Y':
            break
        else:
            continue

    if inp == 2:
        print("You pressed 2!")
        print("Spotify track link should look like this: https://open.spotify.com/album/<gibberish-code>")
        url = str(input("Enter your album url: "))
        with Spotdl() as spotdl_handler:
            spotify_tools = SpotifyHelpers()
            all_songs = spotify_tools.fetch_album(url)
            print(all_songs['name'] + ' - ' + all_songs['label'])
            spotify_tools.write_album_tracks(all_songs, file_name)
            spotdl_handler.download_tracks_from_file(file_name)
            os.system('del' + file_name)
        ch = str(input("Want to exit the program? Press[y/N]: "))
        if ch == 'y' or ch == 'Y':
            break
        else:
            continue

    if inp == 3:
        print("You pressed 3!")
        print("Spotify track link should look like this: https://open.spotify.com/playlist/<gibberish-code>")
        url = str(input("Enter your album url: "))
        with Spotdl() as spotdl_handler:
            spotify_tools = SpotifyHelpers()
            all_songs = spotify_tools.fetch_playlist(url)
            print(all_songs['name'] + ' - ' + all_songs['label'])
            spotify_tools.write_playlist_tracks(all_songs, file_name)
            spotdl_handler.download_tracks_from_file(file_name)
            os.system('del' + file_name)
        ch = str(input("Want to exit the program? Press[y/N]: "))
        if ch == 'y' or ch == 'Y':
            break
        else:
            continue
    if inp == 4:
        print("You pressed 4!")
        print("Write first artist name and then track name for better result:")
        print("For ex: One after None - Slave To Perfection")
        print("It is completely okay if you don't know the artist name...you can just download it by album name.")
        search = str(input("Enter your song name: "))
        with Spotdl(args) as spotdl_handler:
            spotdl_handler.download_track(search)
        ch = str(input("Want to exit the program? Press[y/N]: "))
        if ch == 'y' or ch == 'Y':
            break
        else:
            continue
    if inp == 5:
        os.system('cls')
        print('''

    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

        Welcome To Spotify Songs Downloader 
                
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
                
        Press 1). Download Track by url
        Press 2). Download Album by url 
        Press 3). Download Playlist by url
        Press 4). Download Song by search
        Press 5). To display menu
        Press 6). Exit
                ''')
    if inp == 6:
        break
