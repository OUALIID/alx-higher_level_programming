#!/usr/bin/node
const request = require('request');
const id = process.argv.slice(2);
const url = `https://swapi-api.alx-tools.com/api/films/${id[0]}`;
request(url, (err, response, body) => {
  if (err) {
    return (1);
  }
  console.log(JSON.parse(body).title);
});
