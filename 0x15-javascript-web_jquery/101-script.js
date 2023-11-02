#!/usr/bin/node
/* A JavaScript program that adds, removes, and clears LI items from the list when the user clicks. */
/* global $ */
$(document).ready(function () {
  $('#add_item').click(function () {
    $('UL.my_list').append($('<li>Item</li>'));
  });

  $('#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });

  $('#clear_list').click(function () {
    $('UL.my_list li').remove();
  });
});
