#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const file = process.argv.slice(2);
const url = file;
request(url[0], (err, response, body) => {
  if (err) {
    return;
  }
  fs.writeFile(file[1], body, (date) => {
    process.exit(1);
  });
});
