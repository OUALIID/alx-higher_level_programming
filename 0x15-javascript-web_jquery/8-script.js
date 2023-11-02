#!/usr/bin/node
/* A JavaScript program that fetches the titles of all movies and inserts them using the URL. */
/* global $ */
$(document).ready(function () {
  const Url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(Url, function (data) {
    $.each(data.results, function (index, movie) {
      $('#list_movies').append($('<li>').text(movie.title));
    });
  });
});
