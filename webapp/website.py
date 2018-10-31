'''


    This is the Flask app for the
        "songs and singers" API and website. The API offers
        JSON access to the data, while the website (at
        route '/') offers end-user browsing of the data.
    @author Yuting Su(suy@carleton.edu)
    @author Starr Wang(wangy3@carleton.edu)
    Updated 30 Oct 2018
'''

import sys
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/') 
def get_main_page():
    global api_port
    return flask.render_template('index.html', api_port=api_port)

@app.route('/advanced') 
def get_advanced_page():
    global api_port
    return flask.render_template('advanced.html', api_port=api_port)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {0} host port api-port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    api_port = sys.argv[3]
    app.run(host=host, port=port)

