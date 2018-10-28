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
    var element = document.getElementById('search-icon');
    if (element) {
        element.onclick = onSingersButtonClicked;
    }
}

function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    console.log(baseURL)
    return baseURL;
}

function onSingersButtonClicked() {
    var url = getBaseURL() + '/singers/';
    console.log(url)

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
            tableBody += '<tr>';

            tableBody += '<td><a onclick="getsinger(' + singersList[k]['id'] + ",'"
                            + singersList[k]['singer_name'] + "')\">"
                            + singersList[k]['singer_name'] + '</a></td>';
            tableBody += '</td>';
            tableBody += '</tr>';
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

function getSinger(signerID, singerName) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.
    var url = getBaseURL() + '/singers/' + singerID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(singerInfo) {
        var tableBody = '<tr><th>' + singerName + '</th></tr>';
        for (var k = 0; k < singerInfo.length; k++) {
            tableBody += '<tr>';
            tableBody += '<td>' + singerInfo[k]['name'] + '</td>';
            tableBody += '<td>' + singerInfo[k]['hotness'] + '</td>';
            tableBody += '<td>' + singerInfo[k]['hometown'] + '</td>';
            tableBody += '</tr>';
        }
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

function onSongsButtonClicked() {
    var url = getBaseURL() + '/songs/';

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
            tableBody += '<tr>';

            tableBody += '<td><a onclick="getsong(' + songsList[k]['id'] + ",'"
                            + songsList[k]['name'] + "')\">"
                            + songsList[k]['name'] + '</a></td>';
            tableBody += '</td>';
            tableBody += '</tr>';
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

function getsong(songID, songName) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.
    var url = getBaseURL() + '/songs/' + songID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(songInfo) {
        var tableBody = '<tr><th>' + songName + '</th></tr>';
        for (var k = 0; k < songInfo.length; k++) {
            tableBody += '<tr>';
            tableBody += '<td>' + songInfo[k]['name'] + '</td>';
            tableBody += '<td>' + songInfo[k]['hotness'] + '</td>';
            tableBody += '<td>' + songInfo[k]['album_id'] + '</td>';
            tableBody += '<td>' + songInfo[k]['genre_id'] + '</td>';
            tableBody += '<td>' + songInfo[k]['year'] + '</td>';
            tableBody += '<td>' + songInfo[k]['duration'] + '</td>';
            tableBody += '</tr>';
        }
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

function onAdvancedSongsButtonClicked() {
    var hotness = document.getElementById('hotness');
    var album_name = document.getElementById('album_name');
    var genre_name = document.getElementById('genre_name');
    var year = document.getElementById('year');

    var url = getBaseURL() + '/songs?';
    if (album_name){
        url = url + 'album=' + album_name;
    }
    if(genre_name){
        url = url + 'genre=' + genre_name;
    }
    if(hotness){
        url = url + 'hotness=' + hotness;
    }  
    if(year){
        url = url + 'year=' + year;
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
            tableBody += '<tr>';

            tableBody += '<td><a onclick="getsong(' + songsList[k]['id'] + ",'"
                            + songsList[k]['name'] + "')\">"
                            + songsList[k]['name'] + '</a></td>';
            tableBody += '</td>';
            tableBody += '</tr>';
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

function getsong(songID, songName) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.
    var url = getBaseURL() + '/songs/' + songID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(songInfo) {
        var tableBody = '<tr><th>' + songName + '</th></tr>';
        for (var k = 0; k < songInfo.length; k++) {
            tableBody += '<tr>';
            tableBody += '<td>' + songInfo[k]['name'] + '</td>';
            tableBody += '<td>' + songInfo[k]['hotness'] + '</td>';
            tableBody += '<td>' + songInfo[k]['album_id'] + '</td>';
            tableBody += '<td>' + songInfo[k]['genre_id'] + '</td>';
            tableBody += '<td>' + songInfo[k]['year'] + '</td>';
            tableBody += '<td>' + songInfo[k]['duration'] + '</td>';
            tableBody += '</tr>';
        }
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}