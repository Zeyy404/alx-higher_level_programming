#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(apiUrl, (err, response, body) => {
  if (err) { console.error(err); } else if (response.statusCode !== 200) { console.error(response.statusCode); }
  const movieData = JSON.parse(body);
  const characters = movieData.characters;
  const fetchAndprint = (index) => {
    if (index >= characters.length) { return; }

    const characterUrl = characters[index];
    request(characterUrl, (err, response, body) => {
      if (err) { console.error(err); } else if (response.statusCode !== 200) { console.error(response.statusCode); } else {
        const character = JSON.parse(body);
        console.log(character.name);
        fetchAndprint(index + 1);
      }
    });
  };
  fetchAndprint(0);
});
