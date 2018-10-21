#!/usr/bin/env python3
'''
    books_and_authors_converter.py
    Jeff Ondich, 24 April 2017
    Updated 20 April 2018

    Sample code illustrating a simple conversion of the
    books & authors dataset represented as in books_and_authors.csv,
    into the books, authors, and books_authors tables (in
    CSV form).

    This is trickier than my json_to_tables.py example,
    because in the books.csv file, the authors are implicit
    in the list of books rather than being separated out
    into their own data structure as they are in the
    books_and_authors.json file.
'''
import sys
import re
import csv

def load_from_books_csv_file(csv_file_name):
    ''' Collect all the data from my sample books_and_authors.csv file,
        assembling it into a list of books, a dictionary of authors,
        and a list of book/author ID links. Rather than fully
        documenting the data structures built in this function and
        used in the later functions, I'm going to let you play around
        with it. I recommend just sticking some print statements
        in various places (or set some breakpoints if you use an IDE
        for Python, like PyCharm). You might find it interesting to
        figure out why I needed to use a dictionary for authors, but not
        for books.
    '''
    csv_file = open(csv_file_name)
    reader = csv.reader(csv_file)

    albums = []
    album_names=[]

    genres=[]
    genre_names=[]

    singers = []
    singer_names = []
    extra_singers_names = []
    extra_singer_songs_dic = []

    songs = []
    song_names=[]

    songs_singers = []

    first_row = next(reader)
    for row in reader:

        assert len(row) == 10
        album_name = row[4]
        genre_name = row[7]
        singer_name = row[1]
        song_name = row[8]

        if album_name not in album_names:
            album_names.append(album_name)
            album_id=len(albums)
            album = {'id': album_id, 'name': album_name}
            albums.append(album)

        if genre_name not in genre_names:
            genre_names.append(genre_name)
            genre_id=len(genres)
            genre = {'id': genre_id, 'name': genre_name}
            genres.append(genre)

        feature_singers = singer_name.split(' featuring ')
        singer_name = feature_singers[0]
        if singer_name not in singer_names:
                singer_names.append(singer_name)
                singer_id = len(singers)
                hotness = row[0]
                if hotness=="":
                    hotness = 0
                else:
                    hotness = float(hotness)
                singer = {'id': singer_id, 'name': singer_name, 'hometown': row[3], 'hotness': hotness}
                singers.append(singer)

        # if the song is collobrated by two singers 
        if len(feature_singers) > 1:
            extra_singers_name = feature_singers[1]
            if extra_singers_name not in extra_singers_names:
                extra_singers_names.append(extra_singers_name)
            extra_singer_songs_dic.append({'singer':extra_singers_name, 'song': song_name})

        if song_name not in song_names:
            song_names.append(song_name)
            song_id = len(songs)
            for album in albums:
                if album["name"] == album_name:
                    album_id = album["id"]
                    break
            for genre in genres:
                if genre['name'] == genre_name:
                    genre_id = genre['id']
                    break
            for singer in singers:
                if singer['name'] == singer_name:
                    singer_id = singer['id']

            hotness = row[5]
            if hotness=="":
                hotness = 0
            else:
                hotness = float(hotness)
            songs.append({'id': song_id, 'name': song_name, 'album_id': album_id, 'genre_id':genre_id, 'hotness':hotness, 'year':row[9], 'duration': row[2]})
            songs_singers.append({'song_id': song_id, 'singer_id':singer_id})

    csv_file.close()

    # add the extra singers information to the singer list
    for extra_singer_name in extra_singers_names:
        if extra_singer_name not in singer_names:
            singer = {'id': len(singers), 'name': extra_singer_name, 'hometown': "Not Available", 'hotness': 0}
            singers.append(singer)

    #complete songs_singers
    for extra_singer_song in extra_singer_songs_dic:
        song_id = 0
        singer_id = 0
        for song in songs:
            if song['name'] == extra_singer_song["song"]:
                song_id = song['id']
                break
        for singer in singers:
            if singer['name'] == extra_singer_song["singer"]:
                singer_id = singer["id"]
                break
        songs_singers.append({'song_id': song_id, 'singer_id':singer_id})
    return (albums, genres, singers, songs, songs_singers)


def save_albums_table(albums, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for album in albums:
        album_row = [album['id'], album['name']]
        writer.writerow(album_row)
    output_file.close()

def save_genres_table(genres, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for genre in genres:
        genre_row = [genre['id'], genre['name']]
        writer.writerow(genre_row)
    output_file.close()

def save_songs_table(songs, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for song in songs:
        song_row = [song['id'], song['name'], song['hotness'], song['album_id'], song['genre_id'], song['year'], song['duration']]
        writer.writerow(song_row)
    output_file.close()

def save_songs_singers_table(songs_singers, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for song_singer in songs_singers:
        song_singer_row = [song_singer['song_id'], song_singer['singer_id']]
        writer.writerow(song_singer_row)
    output_file.close()

def save_singers_table(singers, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for singer in singers:
        singer_row = [singer['id'], singer['name'], singer['hotness'], singer['hometown']]
        writer.writerow(singer_row)
    output_file.close()

# def save_authors_table(authors, csv_file_name):
#     ''' Save the books in CSV form, with each row containing
#         (id, last name, first name, birth year, death year), where
#         death year can be NULL. '''
#     output_file = open(csv_file_name, 'w')
#     writer = csv.writer(output_file)
#     for author in sorted(authors, key=authors.get):
#         (last_name, first_name, birth_year, death_year) = author
#         if death_year == '':
#             death_year = 'NULL'
#         author_id = authors[author]
#         author_row = [author_id, last_name, first_name, birth_year, death_year]
#         writer.writerow(author_row)
#     output_file.close()

# def save_linking_table(books_authors, csv_file_name):
#     ''' Save the books in CSV form, with each row containing
#         (book id, author id). '''
#     output_file = open(csv_file_name, 'w')
#     writer = csv.writer(output_file)
#     for book_author in books_authors:
#         books_authors_row = [book_author['book_id'], book_author['author_id']]
#         writer.writerow(books_authors_row)
#     output_file.close()

if __name__ == '__main__':
    albums, genres, singers, songs, songs_singers = load_from_books_csv_file('music.csv')

    save_albums_table(albums, 'albums.csv')
    save_genres_table(genres, 'genres.csv')
    save_songs_table(songs, 'songs.csv')
    save_singers_table(singers, 'singers.csv')
    save_songs_singers_table(songs_singers, 'songs_singers.csv')


    # save_authors_table(authors, 'authors.csv')
    # save_linking_table(books_authors, 'books_authors.csv')