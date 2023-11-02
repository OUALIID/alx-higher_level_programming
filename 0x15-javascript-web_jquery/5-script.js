#!/usr/bin/node
/* A JavaScript program that adds a <li> element to the list when the user clicks the DIV#add_item tag. */
/* global $ */
$(document).ready(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append($('<li>Item</li>'));
  });
});
