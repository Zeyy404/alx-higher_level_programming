#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(apiUrl, (err, response, body) => {
  if (err) { console.error(err); } else if (response.statusCode !== 200) { console.error(response.statusCode); } else { const movieData = JSON.parse(body); console.log(movieData.title); }
});
