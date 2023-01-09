import jiosavan
import os
import song_detail


def main():
    query = input("Enter the song name :\n")

    data_from_search = jiosavan.search_for_query(query)
    print('Songs for the query:',query)
    count = 0
    for song in data_from_search['songs']:
      song_name = song['title']
      song_desc = song['description']
      lang = song['more_info']['language']
      count+=1
      print("{} {}\n     {}".format(count,song_name,song_desc))

    if(len(data_from_search['albums']))!=0:
      print('Albums for the query:',query)
      count = 0
      for song in data_from_search['albums']:
        song_name = song['title']
        song_desc = song['description']
        lang = song['more_info']['language']
        count+=1
        print("{} {}\n     {}\n     Lang :{}".format(count,song_name,song_desc,lang))
    
    if(len(data_from_search['artists']))!=0:
      print('Artists for the query:',query)
      count = 0
      for song in data_from_search['artists']:
        song_name = song['title']
        song_desc = song['description']
        count+=1
        print("{} {}\n     {}\n    ".format(count,song_name,song_desc))

    if(len(data_from_search['playlists']))!=0:
      print('Playlists for the query:',query)
      count = 0
      for song in data_from_search['playlists']:
        song_name = song['title']
        song_desc = song['description']
        lang = song['language']
        count+=1
        print("{} {}\n     {}\n     Lang :{}".format(count,song_name,song_desc,lang))

    print("Type  a, song numbers using ,, ")
    selection_input = input().split(',')

    download_path = 'D:\\practice\\Music\\music'

    for song_num in selection_input[0:]:
      song_id = data_from_search['songs'][int(song_num)-1]['id']
      print(data_from_search['songs'][int(song_num)-1]['title'])
      song_data = jiosavan.get_song(str(song_id))
      song_detail.download_details(song_data, download_path)
      
    



main()