#!/usr/bin/node
/* A JavaScript script that fetches the url and displays the hello value from that fetch in the HTML DIV#hello tag. */
/* global $ */
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.get(url, function (data) {
    $('#hello').text(data.hello);
  });
});
