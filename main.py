from ytmusicapi import YTMusic
from datetime import date

YTMusic.setup(filepath='headers_auth.json', headers_raw= """ <INSERT_HEADERS_HERE> """)
ytmusic = YTMusic('headers_auth.json')

if __name__ == '__main__':

    # Get your Listen Again Songs
    home = ytmusic.get_home(limit=10)
    i = 0
    for items in home: # Finds the Listen Again page
        if items['title'] == 'Listen again':
            break
        i = i + 1
    videoIdList = []
    for songs in home[i]['contents']:
        a = songs.get('videoId')
        if a is not None:
            videoIdList.append(a)
    today = date.today()
    today = today.strftime("%B %d, %Y")  # Date in Month (text) Day, Year
    title = "Weekly ReListener - " + today
    newWeeklyPlaylistID = ytmusic.create_playlist(title=title, description="Created by ReListener at https://github.com/nathaniellamjohnson/ReListener-for-YT-Music on " + today, video_ids=videoIdList)
    foreverPlaylistID = None
    userPlaylists = ytmusic.get_library_playlists(limit=1000)
    for playlists in userPlaylists:
        if playlists['title'] == "Forever ReListener":
            foreverPlaylistID = playlists['playlistId']
    if foreverPlaylistID is not None:
        ytmusic.edit_playlist(playlistId=foreverPlaylistID,
                              description="Created by ReListener at https://github.com/nathaniellamjohnson/ReListener-for-YT-Music, last edited on " + today,
                              addPlaylistId=newWeeklyPlaylistID)
    else:
        ytmusic.create_playlist(title="Forever ReListener",
                                description="Created by ReListener at https://github.com/nathaniellamjohnson/ReListener-for-YT-Music, last edited on " + today,
                                source_playlist=newWeeklyPlaylistID)
