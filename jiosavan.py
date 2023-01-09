import requests
import endpoints
import json
import helpers

albums = ''

def get_song(id):
    song_details = endpoints.song_details_base_url+id
    song = requests.get(song_details).text.encode().decode('unicode-escape')
    song_response = json.loads(song)
    helpers.json_creaters(id, song_response)

    song_data = helpers.format_song(song_response[id])
    return song_data



def search_for_query(query):
    #query = "Saakiya"
    search = endpoints.search_base_url+query
    query_name = query+'.json'
    response = requests.get(search).text
    file_object = json.loads(response)

    helpers.json_creaters(query_name, file_object)

    response_links ={
    'albums' : file_object['albums']['data'],
    'songs' : file_object['songs']['data'],
    'artists' : file_object['artists']['data'],
    'playlists' : file_object['playlists']['data']
    }

    #get_song(songs[1]['id'])
    return response_links

def search_albums(album_id):
    try:
        album_link = endpoints.album_details_base_url+album_id
        album_response = requests.get(album_id)
        if album_response.status_code == 200:
            songs_json = album_response.text.encode().decode('unicode-escape')
            songs_json = json.loads(songs_json)
           # json_for = helpers.json_creaters(album_id, songs_json)
            with open('jsdvdgsds111.json','w',encoding='utf-8') as f:
                json.dump(songs_json,f,ensure_ascii= False,indent =3)
            # file = album_id+'.json'
            # with open(file,'w',encoding='utf-8') as f:
            #     json.dump(songs_json,f,ensure_ascii= False,indent =3)


            #songs_list = songs_json['songs']
            #return songs_list
        else :
            print("Unable fetch the album:",album_response)
    except Exception as er:
        return er


def search_playlists(playlist_id):
    playlist_link = endpoints.playlist_details_base_url+playlist_id
    playlist_response = requests.get(playlist_link)


id = '31987473'
search_albums(id)
print("done")