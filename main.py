from ytmusicapi import YTMusic
from datetime import date
import mgemail

print ("hello")
target_email = "<INSERT_TARGET_EMAIL_HERE>"

# requires a headers_raw.txt with raw header data to get
with open('INSERT_DIRECT_PATH_TO headers_raw.txt') as headers_raw_file:
    headers_raw_text = headers_raw_file.read()

try:
    YTMusic.setup(filepath='headers_auth.json', headers_raw= headers_raw_text)
    ytmusic = YTMusic('headers_auth.json')
except Exception:
    #Problem with authentication
    mgemail.send_email(target_email, "ReListener Playlist Update Failed", "Problem with authentication, please check "
                                                                        "headers_raw.txt and get new headers as "
                                                                        "according to "
                                                                        "https://github.com/sigma67/ytmusicapi "
                                                                        "\n\n\n- Nathaniel From ReListener" )
    quit(1)



def get_section_of_home(home_list, sec_name):
    i = 0
    for items in home_list:  # Finds the Listen Again page
        if items['title'] == sec_name:
            break
        i = i + 1
    return i


def get_all_songs_in_section(home_list, index_of_section):
    list_of_songs_to_append_to = []
    for songs in home_list[index_of_section]['contents']:
        a = songs.get('videoId')
        if a is not None:
            list_of_songs_to_append_to.append(a)
    return list_of_songs_to_append_to


def clean_today_date():
    # returns string for date in format of Month(text) Day, Year
    today = date.today()
    today = today.strftime("%B %d, %Y")
    return today


def update_forever_playlist(video_id_list):
    # Get the forever playlist id / if doesn't exist, make one
    foreverplaylistid = None
    userplaylists = ytmusic.get_library_playlists(limit=1000)

    for playlist in userplaylists:
        if playlist['title'] == "Forever ReListener":
            foreverplaylistid = playlist['playlistId']

    if foreverplaylistid is None:
        # No forever playlist found, make one & put all the video ids from the weekly in
        foreverplaylistid = ytmusic.create_playlist(title="Forever ReListener",
                                                    description="Created by ReListener at "
                                                                "https://github.com/nathaniellamjohnson/ReListener"
                                                                "-for-YT-Music, last edited on " + clean_today_date(),
                                                    video_ids=videoIdList)
        return foreverplaylistid

    # If forever playlist is present
    # take song ids, check against song ids of forever playlist, remove duplicates
    foreverplaylist = ytmusic.get_playlist(playlistId=foreverplaylistid, limit=10000)
    foreverplaylistsongids = []
    for obj in foreverplaylist['tracks']:
        foreverplaylistsongids.append(obj['videoId'])
    # Loop through video id list
    valid_ids = []
    for song in video_id_list:
        if song not in foreverplaylistsongids:
            valid_ids.append(song)
    if valid_ids:
        ytmusic.add_playlist_items(playlistId=foreverplaylistid, videoIds=valid_ids)
        ytmusic.edit_playlist(playlistId= foreverplaylistid, description="Created by ReListener at https://github.com/nathaniellamjohnson/ReListener-for"
                                      "-YT-Music, last edited on " + clean_today_date())
    return foreverplaylistid


if __name__ == '__main__':
    home = ytmusic.get_home(limit=10)
    indexOfListenAgain = get_section_of_home(home, 'Listen again')

    videoIdList = get_all_songs_in_section(home, indexOfListenAgain)

    newWeeklyPlaylistID = ytmusic.create_playlist(title="Weekly ReListener - " + clean_today_date(),
                                                  description="Created by ReListener at "
                                                              "https://github.com/nathaniellamjohnson/ReListener-for"
                                                              "-YT-Music on " + clean_today_date(),
                                                  video_ids=videoIdList)

    foreverplaylistid = update_forever_playlist(videoIdList)
    mgemail.send_email(target_email, "ReListener Playlist Update Success", "See the weekly playlist here: https://music.youtube.com/playlist?list=" + newWeeklyPlaylistID + "\n \n See the updated forever playlist here: https://music.youtube.com/playlist?list=" + foreverplaylistid + "\n\n\n- Nathaniel From ReListener"  )
