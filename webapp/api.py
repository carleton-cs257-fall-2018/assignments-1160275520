#!/usr/bin/env python3
'''
Web Application Phase 5 Homework
    @author Yuting Su(suy@carleton.edu)
    @author Starr Wang(wangy3@carleton.edu)
    2018-10-21
'''
import sys
import flask
import json
import config
import psycopg2


app = flask.Flask(__name__, static_folder='static', template_folder='templates')

def get_connection():
    '''
    Returns a connection to the database described
    in the config module. Returns None if the
    connection attempt fails.
    '''
    connection = None
    try:
        connection = psycopg2.connect(database=config.database,
                                      user=config.user,
                                      password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
    return connection

def get_select_query_results(connection, query, parameters=None):
    '''
    Executes the specified query with the specified tuple of
    parameters. Returns a cursor for the query results.
    Raises an exception if the query fails for any reason.
    '''
    cursor = connection.cursor()
    if parameters is not None:
        cursor.execute(query, parameters)
    else:
        cursor.execute(query)
    return cursor

@app.after_request
def set_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/')
def hello():
    return 'Welcome to Musify!'

@app.route('/singers/<singer_id>')
def get_singer_by_id(singer_id):
    '''
    Returns the singer resource for the singer with the specified id.

    See get_singer above for a description of the
    singer resource representation.
    '''
    query = '''SELECT * FROM singers WHERE id = %s'''

    singer = {}
    connection = get_connection()
    if connection is not None:
        try:
            cursor = get_select_query_results(connection, query, (singer_id,))
            row = next(cursor)
            if row is not None:
                singer = {"id":row[0], "singer_name":row[1], "hotness":row[2], "hometown":row[3]}
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()

    return json.dumps(singer)


@app.route('/singers')
def get_singers():
    '''
    Returns a list of all the singers with optional search query. 
    The match is case-insensitive.

    *singer_name [optional]: return singers that contains specific query singer_name string

    *hotness [optional]: return singers with hotness larger than the query hotness

    *hometown [optional] - return singers that contains specific query hometown string

    For example: singers?singer_name=emilio&hometown=texas
                search for singers whose name contains "emilio" 
                and their hometwon's name contains "texas".
    
    See get_singers above for a description of the
    singer resource representation.
    '''

    singer_list = []

    query_singer_name = flask.request.args.get('singer_name')
    query_hotness = flask.request.args.get('hotness')
    query_hometown = flask.request.args.get('hometown')

    query_string = ""

    if query_singer_name is not None:
        query_string += "UPPER(name) LIKE '%%' || UPPER('" + str(query_singer_name) + "')|| '%%'"
    if query_hotness is not None:
        if query_string!="":
            query_string += " AND "
        query_string += "hotness >" + str(query_hotness)
    if query_hometown is not None:
        if query_string!="":
            query_string += " AND "
        query_string += "UPPER(hometown) LIKE '%%' || UPPER('" + str(query_hometown) + "')|| '%%'"


    query = '''SELECT *
               FROM singers
               WHERE ''' + query_string

    print(query)

    connection = get_connection()
    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                singer = {"id":row[0], "singer_name":row[1], "hotness":row[2], "hometown":row[3]}
                singer_list.append(singer)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()

    return json.dumps(singer_list)


@app.route('/songs/<song_id>')
def get_song_by_id(song_id):
    '''
    Returns the song resource for the song with the specified id.

    See get_songs above for a description of the
    song resource representation.
    '''
    query = '''SELECT * FROM songs WHERE id = %s'''

    song = {}
    connection = get_connection()
    if connection is not None:
        try:
            cursor = get_select_query_results(connection, query, (song_id,))
            row = next(cursor)
            if row is not None:
                song = {"id":row[0], "song_name":row[1], "hotness":row[2],"album_id":row[3], "genre_id":row[4], "release_year":row[5], "duration": row[6]}
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()

    return json.dumps(song)

@app.route('/songs')
def get_songs():
    '''
    Returns a list of all the songs with optional search query. 
    The match is case-insensitive.

    *song_name[optional]: return songs whose name contains specific query song_name string

    *singer_name[optional]: return songs sung by singers whose name contains specific query singer_name string

    *hotness [optional]: return songs with hotness larger than the query hotness

    *genre [optional]: return songs with specific query genre
        
    *year [optional]: return songs with specific query year

    *album [optional]: return songs from albums whose name contains specific query album string

    For example: /songs?genre=jazz&album=love&year=1993 
                searches for songs whose genre is jazz, 
                from albums whose name contains "love" and published in 1993. 

    See get_songs above for a description of the
    singer resource representation.
    '''
    song_list = []

    query_song_name = flask.request.args.get('song_name')
    query_hotness = flask.request.args.get('hotness')
    query_year = flask.request.args.get('year')
    query_album = flask.request.args.get('album')
    query_genre = flask.request.args.get('genre')
    query_singer = flask.request.args.get('singer_name')

    query_string = ""
    from_string = "songs"

    if query_song_name is not None:
        query_string += "UPPER(song_name) LIKE '%%' || UPPER('" + str(query_song_name) + "')|| '%%'"
    if query_hotness is not None:
        if query_string!="":
            query_string += " AND "
        query_string += "songs.hotness >" + str(query_hotness)
    if query_year is not None:
        if query_string!="":
            query_string += " AND "
        query_string += "year =" + str(query_year)

    if query_album is not None:
        from_string+=", albums"
        if query_string!="":
            query_string += " AND "
        query_string += "songs.album_id=albums.id AND UPPER(albums.name) LIKE '%%' || UPPER('" + str(query_album) + "')|| '%%'" 

    if query_genre is not None:
        from_string+=", genres"
        if query_string!="":
            query_string += " AND "
        query_string += "songs.genre_id=genres.id AND UPPER(genres.name) LIKE '%%' || UPPER('" + str(query_genre) + "')|| '%%'" 

    if query_singer is not None:
        from_string+=", singers, songs_singers"
        if query_string!="":
            query_string += " AND "
        query_string += "singers.id=songs_singers.singer_id AND songs_singers.song_id=songs.id AND UPPER(singers.name) LIKE '%%' || UPPER('" + str(query_singer) + "')|| '%%'" 


    query = '''SELECT *
               FROM ''' + from_string + ''' WHERE ''' + query_string


    connection = get_connection()
    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                song = {"id":row[0], "song_name":row[1], "hotness":row[2],"album_id":row[3], "genre_id":row[4], "release_year":row[5], "duration": row[6]}
                song_list.append(song)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()

    return json.dumps(song_list)


@app.route('/albums')
def get_albums():
    '''
    Returns the list of albums in the database. An album resource
    will be represented by a JSON dictionary with keys 'id' (int) and
    'name' (string).
    Returns an empty list if there's any database failure.
    '''
    query = 'SELECT * FROM albums'
    album_list = []
    connection = get_connection()
    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                album = {'id':row[0], 'name':row[1]}
                album_list.append(album)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()

    return json.dumps(album_list)

@app.route('/genres')
def get_genres():
    '''
    Returns the list of genres in the database. A genre resource
    will be represented by a JSON dictionary with keys 'id' (int) and
    'name' (string).
    Returns an empty list if there's any database failure.
    '''
    query = 'SELECT * FROM genres'
    genre_list = []
    connection = get_connection()
    if connection is not None:
        try:
            for row in get_select_query_results(connection, query):
                genre = {'id':row[0], 'name':row[1]}
                genre_list.append(genre)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()

    return json.dumps(genre_list)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
