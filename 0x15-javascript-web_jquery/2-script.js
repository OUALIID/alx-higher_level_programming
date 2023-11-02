#!/usr/bin/node
/* A JavaScript script that updates the header element's text color to red when the user clicks the DIV#red_header tag */
/* global $ */
$(document).ready(function () {
  $('#red_header').css('color', '#FF0000');
});
