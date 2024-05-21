#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
request(apiUrl, (err, response, body) => {
  if (err) { console.error(err); } else if (response.statusCode !== 200) { console.error(response.statusCode); } else {
    const films = JSON.parse(body).results;
    const count = films.reduce((acc, film) => {
      return acc + (film.characters.includes(wedgeAntillesUrl) ? 1 : 0);
    }, 0);
    console.log(count);
  }
});
