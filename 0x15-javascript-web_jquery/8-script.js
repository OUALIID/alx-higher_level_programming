#!/usr/bin/node
/* A JavaScript program that fetches the titles of all movies and inserts them using the URL. */
/* global $ */    
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$(document).ready(function () {
    $.get(url, function (data) {
        $.each(data.results, function (index, movie) {
            $('#list_movies').append($('<li>').text(movie.title));
        });
    });
});
