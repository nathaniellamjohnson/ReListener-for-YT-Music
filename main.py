from ytmusicapi import YTMusic
YTMusic.setup(filepath='headers_auth.json', headers_raw = "<INSERT_HEADERS_HERE>")

if __name__ == '__main__':
    ytmusic = YTMusic()
    search = ytmusic.search("<INSERT_QUERY_HERE>")
    print(search)


