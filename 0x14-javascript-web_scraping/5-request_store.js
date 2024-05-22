#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, (err, response, body) => {
  if (err) { console.error(err); } else if (response.statusCode !== 200) { console.error(response.statusCode); } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
      if (err) { console.error(err); process.exit(1); }
    });
  }
});
