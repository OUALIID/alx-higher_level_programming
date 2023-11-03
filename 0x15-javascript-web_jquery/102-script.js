#!/usr/bin/node
/* A JavaScript script that fetches and prints how to say "hello" depending on the language. */
/* global $ */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;
    $('#hello').empty();
    $.get(url, function (data) {
      $('#hello').append(data.hello);
    });
  });
});
