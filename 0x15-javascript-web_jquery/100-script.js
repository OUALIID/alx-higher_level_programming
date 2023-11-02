#!/usr/bin/node
/* A JavaScript program that updates the text color of a <header> element to red. */
document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');
  if (header) {
    header.style.color = '#FF0000';
  }
});
