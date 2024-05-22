#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (err, response, body) => {
  if (err) { console.error(err); } else if (response.statusCode !== 200) { console.error(response.statusCode); }
  const todos = JSON.parse(body);
  console.log(todos
    .filter(todo => todo.completed) // Filter only completed todos
    .reduce((acc, todo) => {
      acc[todo.userId] = (acc[todo.userId] || 0) + 1;
      return acc;
    }, {}));
});
