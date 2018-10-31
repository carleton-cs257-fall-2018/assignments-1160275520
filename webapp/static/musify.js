/*
    Web Application Phase 6 Homework
    musify.js
    @author Yuting Su(suy@carleton.edu)
    @author Starr Wang(wangy3@carleton.edu)
 ```@Jeff Ondich
 * Updated, 30 Oct 2018

 *
 * This is the Javascript file for Musify. 
 */


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

//Get the list of singer dictionaries 
function onSingersButtonClicked() {
    var searchWord = document.getElementById('search-bar').value;

    var url = getBaseURL() + '/singers?singer_name=' + searchWord;

    fetch(url, {method: 'get'})

    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of singer dictionaries).
    .then((response) => response.json())

    .then(function(singersList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < singersList.length; k++) {
            if (k%4 == 0){
                tableBody += '<tr>';
            }
            tableBody += '<td><a class="tablebody" onclick="getSinger(' + singersList[k]['id'] + ",'"
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

//Get the information about a specific singer  
function getSinger(singerID, singerName) {
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
    })

    .catch(function(error) {
        console.log(error);
    });
}

//Get the list of song dictionaries 
function onSongsButtonClicked() {
    var searchWord = document.getElementById('search-bar').value;

    var url = getBaseURL() + '/songs?song_name=' + searchWord;

    fetch(url, {method: 'get'})

    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of song dictionaries).
    .then((response) => response.json())

    .then(function(songsList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < songsList.length; k++) {
            if (k%4 == 0){
                tableBody += '<tr>';
            }
            tableBody += '<td><a class="tablebody" onclick="getSong(' + songsList[k]['id'] + ",'"
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

//Get the information about a specific song  
function getSong(songID, songName) {
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
    })

    .catch(function(error) {
        console.log(error);
    });
}

//Get the list of song dictionaries based on the key word in search
function onAdvancedSongsButtonClicked() {
    var song_name = document.getElementById('song_name').value;
    var singer = document.getElementById('singer').value;
    var song_hotness = document.getElementById('song_hotness').value;
    var album_name = document.getElementById('album').value;
    var genre_name = document.getElementById('genre').value;
    var year = document.getElementById('year').value;

    var hasKey = false;

    //generate the url to call api
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
        url = url + 'singer_name=' + singer;
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

    fetch(url, {method: 'get'})

    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of song dictionaries).
    .then((response) => response.json())

    .then(function(songsList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < songsList.length; k++) {
            if (k%4 == 0){
                tableBody += '<tr>';
            }
            tableBody += '<td><a class="tablebody" onclick="getSong(' + songsList[k]['id'] + ",'"
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

//Get the list of singer dictionaries based on the key word in search
function onAdvancedSingersButtonClicked() {
    var singer_name = document.getElementById('singer_name').value;
    var singer_hotness = document.getElementById('singer_hotness').value;
    var hometown = document.getElementById('hometown').value;

    var hasKey = false;

    //generate the url to call api
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

    fetch(url, {method: 'get'})

    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of singer dictionaries).
    .then((response) => response.json())

    .then(function(singersList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < singersList.length; k++) {
            if (k%4 == 0){
                tableBody += '<tr>';
            }
            tableBody += '<td><a class="tablebody" onclick="getSinger(' + singersList[k]['id'] + ",'"
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