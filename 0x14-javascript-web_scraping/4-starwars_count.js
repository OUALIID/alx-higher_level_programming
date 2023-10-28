#!/usr/bin/node
const request = require('request');
const id = process.argv.slice(2);
const url = id[0];

request(url, (err, response, body) => {
  if (err) {
    return;
  }
  const films = JSON.parse(body).results;
  const characterId = '18';
  let total = 0;

  for (const film of films) {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      total++;
    }
  }
  console.log(total);
});
