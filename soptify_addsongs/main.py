import requests
from bs4 import BeautifulSoup
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
CLIENT_ID = "78243ee5e8cc4923babb7e864ab09cff"
CLIENT_SECRET = "29014bc824c9486da99222734cab6172"
# user_date = input("Enter the date you wannna listen on YYYY-MM-DD format \n")
# # print(f"https://www.billboard.com/charts/hot-100/{user_date}")
# billboard_text = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}").text
bob_dai = requests.get("https://www.theguardian.com/music/2020/apr/09/bob-dylans-50-greatest-songs-ranked").text
soup = BeautifulSoup(bob_dai,"html.parser")
print(soup)
# song_name = soup.select(selector="#50-changing-of-the-guards-1978")
# song_name = soup.select(selector=".lrv-u-width-100p .o-chart-results-list__item #title-of-a-story")
# artist_name = soup.select(selector=f".lrv-u-width-100p .o-chart-results-list__item span.c-label.a-no-trucate")
# #
# print(song_name)
# song_list = [song.getText().strip() for song in song_name]
# print(song_list)
# artist_list = [artist.getText().strip() for artist in artist_name]
# uri_list = []
#
# PLAYLIST_NAME = f"Bob top 50"
# sp = spotipy.Spotify(
#     auth_manager= SpotifyOAuth(
#         scope= "playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id= CLIENT_ID,
#         client_secret= CLIENT_SECRET,
#         show_dialog= True,
#         cache_path= "token.txt"
#     )
# )
#
# # results = sp.search(q=f'track: Najeek artist: Bartika Eam Rai', type='track')
# # results = sp.search(q=f'track: {song_list[0]} artist: {artist_list[0]}', type='track')
# # result_uri = results["tracks"]["items"][0]["uri"]
#
# for el in range(len(song_list)):
#     results = sp.search(q=f'track: {song_list[el]} artist: {artist_list[el]}', type='track')
#     result_uri = results["tracks"]["items"][0]["uri"]
#     uri_list.append(result_uri)
#
# #Creating Playlist
# # user = sp.current_user()
# # print(user)
# user_id = sp.current_user()["id"]
# # print(user_id)
# playlist = sp.user_playlist_create(user=user_id,name=PLAYLIST_NAME,public=False)
# playlist_id = playlist["id"]
# # print(playlist)
# sp.playlist_add_items(playlist_id=playlist_id,items=uri_list)
# for link in uri_list:
# print(result_uri)
# print(uri_list)
# print(result_uri)
# print(sp.current_user()['display_name'])
# results = sp.search(q=f'track: {song_list[0]} artist: {artist_list[0]}', type='track')

# qfcvmndalhq8pvqkh3zz16j4v
# qfcvmndalhq8pvqkh3zz16j4v
# pprint(results)
# print(result_uri)
# pprint(results)
# print(song_list)
# print(artist_list)
# print(song_name.getText().strip())
# collection = {
#     ""
# }
# print(artist_name)
#

# print(song_list)
# print(song_name.strip())
# print(artist_name.strip())
# print(soup)








# http://example.com/?code=AQCbo3jB_uyT-LKi7oThPjGhclGbrxH72GgnMV8AMFrh_NDPa6jD0-P51PNU_dJeNBp3e4tXQwuhvgKeEEoW6iA_VkzEltkc8CJaiobifbtq8aKAb4fOq4yfKm8JVQwP1Q8x7DHmBDDpwl5oal8P1HsSH3lMQZV-uoByvwtEIej7tNb4pvUQrtjMHvU3i3o