#!/usr/bin/node
const request = require('request');
const id = process.argv.slice(2);
const url = id[0];
request(url, (err, response, body) => {
  if (err) {
    console.log('error_1');
  }
  const films = JSON.parse(body).results;
  let total = 0;
  for (const film of films) {
    if (film.characters) {
      const date = film.characters;
      for (const cur of date) {
        if (cur === 'https://swapi-api.alx-tools.com/api/people/18/') {
          total++;
        }
      }
    }
  }
  console.log(total);
});
