import requests
import utils

def getData(artist_id):
    print("[#1] Data: Getting data...")

    url = "https://api.deezer.com/artist/"+str(artist_id)

    artist_json = requests.get(url).json()
    artist_info = [artist_json["name"], artist_json["link"]]
    artist_album_count = artist_json["nb_album"]

    url = "https://api.deezer.com/artist/"+str(artist_id)+"/albums"

    artist_albuns_json = requests.get(url).json()
    artist_albuns_data = artist_albuns_json["data"]

    open("test.txt", "w").write(str(artist_albuns_json))
    while ('next' in artist_albuns_json):
        artist_albuns_json = requests.get(artist_albuns_json["next"]).json()
        artist_albuns_data += artist_albuns_json["data"]
    albuns_id_array = __getArtistAlbunsIdArray(artist_albuns_data)
    albuns_library, songs_library = __getSongsOfAlbuns(albuns_id_array, artist_id)

    print("[#1] Data:",len(albuns_library),"/",artist_album_count,"albuns had been found.")
    print("[#1] Data:",len(songs_library),"musics had been found.")
    
    return [artist_info, albuns_library, songs_library]

def __getArtistAlbunsIdArray(artist_albuns_data):
    albuns_id_array = []

    for obj in artist_albuns_data:
        albuns_id_array.append(obj["id"])

    albuns_id_array = utils.get_unique_numbers(albuns_id_array)
    return albuns_id_array

def __getSongsOfAlbuns(albuns_id_array, artist_id):
    # albuns_library = album_info
    # songs_library = songs_info
    # albuns_library = [title,duration,release_date,fans,link]
    # songs_library = [name,duration,rank,link]

    albuns_library = []
    songs_library = []

    for album_id in albuns_id_array:
        album_info = []
        song_info = []
        url = "https://api.deezer.com/album/"+str(album_id)
        album_json = requests.get(url).json()

        album_info = [album_json["title"],album_json["duration"],album_json["release_date"],album_json["fans"],album_json["link"]]
        albuns_library.append(album_info)

        tracks = album_json["tracks"]

        for song in tracks["data"]:
            song_artist_temp = song["artist"]
            if int(song_artist_temp["id"]) == artist_id:
                song_info = [song["title"],song["duration"],song["rank"],song["link"]]
                songs_library.append(song_info)

    return albuns_library, songs_library