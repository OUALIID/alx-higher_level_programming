#!/usr/bin/node
/* JavaScript script that fetches and prints how to say "Hello" when the user clicks #btn_translate or presses ENTER */
/* global $ */
$(document).ready(function () {
  $('#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      $('#btn_translate').click();
    }
  });

  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;
    $('#hello').empty();
    $.get(url, function (date) {
      $('#hello').append(date.hello);
    });
  });
});
