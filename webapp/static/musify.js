/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 4 May 2018
 *
 * A little bit of Javascript showing one small example of AJAX
 * within the "books and authors" sample for Carleton CS257,
 * Spring Term 2017.
 *
 * This example uses a very simple-minded approach to Javascript
 * program structure, which suffers from the problem of
 * "global namespace pollution". We'll talk more about this after
 * you get a feel for some Javascript basics.
 */

// IMPORTANT CONFIGURATION INFORMATION
// The contents of getBaseURL below reflects our assumption that
// the web application (books_website.py) and the API (books_api.py)
// will be running on the same host but on different ports.
//
// But if you take a look at the contents of getBaseURL, you may
// ask: where does the value of api_port come from? The answer is
// a little bit convoluted. (1) The command-line syntax of
// books_website.py includes an argument for the API port;
// and (2) the index.html Flask/Jinja2 template includes a tiny
// bit of Javascript that declares api_port and assigns that
// command-line API port argument to api_port. This happens
// before books.js is loaded, so the functions in books.js (like
// getBaseURL) can access api_port as needed.

initialize();

function initialize() {

    var singers = document.getElementById('singers');
    if (singers) {
        singers.onclick = onSingersButtonClicked;
    }
    var songs = document.getElementById('songs');
    if (songs) {
        songs.onclick = onSongsButtonClicked;
    }
    var advanced_songs = document.getElementById('advanced_songs');
    if (advanced_songs) {
        advanced_songs.onclick = onAdvancedSongsButtonClicked;
    }
    var advanced_singers = document.getElementById('advanced_singers');
    if (advanced_singers) {
        advanced_singers.onclick = onAdvancedSingersButtonClicked;
    }
}

function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    console.log(baseURL)
    return baseURL;
}

function onSingersButtonClicked() {
    var searchWord = document.getElementById('search-bar').value;

    var url = getBaseURL() + '/singers?singer_name=' + searchWord;
    // Send the request to the Books API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(singersList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < singersList.length; k++) {
            if (k%4 == 0){
                tableBody += '<tr>';
            }
            tableBody += '<td><a onclick="getSinger(' + singersList[k]['id'] + ",'"
                            + singersList[k]['singer_name'] + "')\">"
                            + singersList[k]['singer_name'] + '</a></td>';
            if ((k+1)%4 == 0){
                tableBody += '</tr>';
            }            
        }

        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })
    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function getSinger(singerID, singerName) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.
    var url = getBaseURL() + '/singers/' + singerID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(singerInfo) {
        var tableBody = '<tr><th scope="col">Singer Name</th><th scope="col">Hotness</th><th scope="col">Hometown</th></tr>'      
        tableBody += '<tr>';
        tableBody += '<td>' + singerInfo['singer_name'] + '</td>';
        tableBody += '<td>' + singerInfo['hotness'] + '</td>';
        tableBody += '<td>' + singerInfo['hometown'] + '</td>';
        tableBody += '</tr>';        
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
        console.log("singers2")
    })

    .catch(function(error) {
        console.log(error);
    });
}

function onSongsButtonClicked() {
    var searchWord = document.getElementById('search-bar').value;

    var url = getBaseURL() + '/songs?song_name=' + searchWord;

    // Send the request to the Books API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(songsList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < songsList.length; k++) {
            if (k%4 == 0){
                tableBody += '<tr>';
            }
            tableBody += '<td><a onclick="getSong(' + songsList[k]['id'] + ",'"
                            + songsList[k]['song_name'] + "')\">"
                            + songsList[k]['song_name'] + '</a></td>';
            tableBody += '</td>';
            if ((k+1)%4 == 0){
                tableBody += '<tr>';
            }
        }

        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function getSong(songID, songName) {

    var searchWord = document.getElementById('search-bar').value;
    console.log(searchWord)
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.
    var url = getBaseURL() + '/songs/' + songID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(songInfo) {
        var tableBody = '<tr><th scope="col">Song Name</th><th scope="col">Hotness</th><th scope="col">Release Year</th><th scope="col">Duration</th></tr>';
        tableBody += '<tr>';
        tableBody += '<td>' + songInfo['song_name'] + '</td>';
        tableBody += '<td>' + songInfo['hotness'] + '</td>';
        tableBody += '<td>' + songInfo['release_year'] + '</td>';
        tableBody += '<td>' + songInfo['duration'] + '</td>';
        tableBody += '</tr>';
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
        console.log("song2")
    })

    .catch(function(error) {
        console.log(error);
    });
}

function onAdvancedSongsButtonClicked() {
    var song_name = document.getElementById('song_name').value;
    var singer = document.getElementById('singer').value;
    var song_hotness = document.getElementById('song_hotness').value;
    var album_name = document.getElementById('album').value;
    var genre_name = document.getElementById('genre').value;
    var year = document.getElementById('year').value;

    var hasKey = false;

    var url = getBaseURL() + '/songs?';
    if (song_name){
        if (hasKey == true){
            url = url+"&";
        }
        url = url + 'song_name=' + song_name;
        hasKey = true;
    }
    if (singer){
        if (hasKey == true){
            url = url+"&";
        }
        url = url + 'singer=' + singer;
        hasKey = true;
    }
    if (album_name){
        if (hasKey == true){
            url = url+"&";
        }
        url = url + 'album=' + album_name;
        hasKey = true;
    }
    if(genre_name){
        if (hasKey == true){
            url = url+"&";
        }
        url = url + 'genre=' + genre_name;
        hasKey = true;
    }
    if(song_hotness){
        if (hasKey == true){
            url = url+"&";
        }
        url = url + 'hotness=' + song_hotness;
        hasKey = true;
    }  
    if(year){
        if (hasKey == true){
            url = url+"&";
        }
        url = url + 'year=' + year;
        hasKey = true;
    }

    // Send the request to the Books API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(songsList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < songsList.length; k++) {
            if (k%4 == 0){
                tableBody += '<tr>';
            }
            tableBody += '<td><a onclick="getSong(' + songsList[k]['id'] + ",'"
                            + songsList[k]['song_name'] + "')\">"
                            + songsList[k]['song_name'] + '</a></td>';
            tableBody += '</td>';
            if ((k+1)%4 == 0){
                tableBody += '<tr>';
            }
        }

        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function onAdvancedSingersButtonClicked() {
    var singer_name = document.getElementById('singer_name').value;
    var singer_hotness = document.getElementById('singer_hotness').value;
    var hometown = document.getElementById('hometown').value;

    var hasKey = false;

    var url = getBaseURL() + '/singers?';
    if (singer_name){
        if (hasKey == true){
            url = url+"&";
        }
        url = url + 'singer_name=' + singer_name;
        hasKey = true;
    }
    if(singer_hotness){
        if (hasKey == true){
            url = url+"&";
        }
        url = url + 'hotness=' + singer_hotness;
        hasKey = true;
    }  
    if(hometown){
        if (hasKey == true){
            url = url+"&";
        }
        url = url + 'hometown=' + hometown;
        hasKey = true;
    }

    // Send the request to the Books API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(singersList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < singersList.length; k++) {
            if (k%4 == 0){
                tableBody += '<tr>';
            }
            tableBody += '<td><a onclick="getSinger(' + singersList[k]['id'] + ",'"
                            + singersList[k]['singer_name'] + "')\">"
                            + singersList[k]['singer_name'] + '</a></td>';
            if ((k+1)%4 == 0){
                tableBody += '</tr>';
            }            
        }
        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })
    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}