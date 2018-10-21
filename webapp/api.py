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

@app.route('/singers')
def get_singers():
    '''
    Returns the list of singers in the database. A singer resource
    will be represented by a JSON dictionary with keys 'id' (int),
    'singer_name' (string), 'hometown' (string), and 'hotness' (float).
    Returns an empty list if there's any database failure.
    '''
    query = 'SELECT * FROM singers'
    singer_list = []
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

@app.route('/singers?name=<singer_name>')
def get_singers_by_name(singer_name):
    '''
    Returns a list of all the singers with names containing
    the specified name. The match is case-insensitive.
    
    See get_singers above for a description of the
    singer resource representation.
    '''
    print(singer_name)
    query = '''SELECT *
               FROM singers
               WHERE UPPER(name) LIKE  LIKE '%%' || UPPER(%s) || '%%' 
               ORDER BY name'''

    singer_list = []
    connection = get_connection()
    if connection is not None:
        try:
            for row in get_select_query_results(connection, query, (name,)):
                singer = {"id":row[0], "singer_name":row[1], "hotness":row[2], "hometown":row[3]}
                singer_list.append(singer)
        except Exception as e:
            print(e, file=sys.stderr)
        connection.close()

    return json.dumps(singer_list)



@app.route('/songs')
def get_songs():
    '''
    Returns the list of songs in the database. A song resource
    will be represented by a JSON dictionary with keys 'id' (int),
    'song_name' (string), 'hotness' (float), 'album_id' (int), 'genre_id' (int), 
    'release_year' (int), and 'duration' (float).
    Returns an empty list if there's any database failure.
    '''
    query = 'SELECT * FROM songs'
    song_list = []
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

@app.route('/songs?name=<name>')
def get_songs_by_name(name):
    '''
    Returns a list of all the songs with names containing
    the specified name. The match is case-insensitive.
    
    See get_songs above for a description of the
    singer resource representation.
    '''
    query = '''SELECT *
               FROM songs
               WHERE UPPER(song_name) LIKE '%%' || UPPER("world") || '%%'
               ORDER BY song_name'''

    song_list = []
    connection = get_connection()
    if connection is not None:
        try:
            for row in get_select_query_results(connection, query, (name,)):
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
