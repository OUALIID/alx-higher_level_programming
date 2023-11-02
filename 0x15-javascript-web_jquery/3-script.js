#!/usr/bin/node
/* A JavaScript program that adds the red class to the <header> element when the user clicks on the DIV#red_header tag. */
/* global $ */
$(document).ready(function() {
    $('#red_header').click(function() {
        $('header').addClass('red');
   });
});
