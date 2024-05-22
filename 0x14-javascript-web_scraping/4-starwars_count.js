#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (err, response, body) => {
  if (err) { console.error(err); } else if (response.statusCode !== 200) { console.error(response.statusCode); } else {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
