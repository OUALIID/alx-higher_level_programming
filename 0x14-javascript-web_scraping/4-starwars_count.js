#!/usr/bin/node
const request = require('request');
const id = process.argv.slice(2);
const url = id[0];
request(url, (err, response, body) => {
  if (err) {
    return;
  }
  const films = JSON.parse(body).results;
  let total = 0;
  for (const film of films) {
    if (film.characters) {
      const date = film.characters;
      for (const cur of date) {
        if (cur.endsWith('/18/')) {
          total++;
        }
      }
    }
  }
  console.log(total);
});
