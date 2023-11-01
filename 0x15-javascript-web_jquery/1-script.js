#!/usr/bin/node
/* Update the <header> element's text color to red without using document.querySelector. */
/* global $ */
$(document).ready(function () {
  $('header').css('color', '#FF0000');
});
