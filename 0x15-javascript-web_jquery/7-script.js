#!/usr/bin/node
/* A JavaScript program that fetches the character name from a URL. */
/* global $ */
const Url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$(document).ready(function () {
  $.get(Url, function (data) {
    $('#character').text(data.name);
  });
});
