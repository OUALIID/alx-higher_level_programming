#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2);
request(url[0], (error, response) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
