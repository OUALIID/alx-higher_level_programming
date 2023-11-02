#!/usr/bin/node
/* A JavaScript program that updates the text of the <header> element to New Header!!! When user clicks on DIV#update_header. */
/* global $ */
$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
