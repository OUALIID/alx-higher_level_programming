#!/usr/bin/node
/** A JavaScript program that always switches the class of a <header> element to one: red or green. */
$(document).ready(function() {
    $('#toggle_header').click(function() {
        const header = $('header');
        if (header.hasClass('red')) {
            header.removeClass('red').addClass('green');
        } else {
            header.removeClass('green').addClass('red');
        }
    });
});
