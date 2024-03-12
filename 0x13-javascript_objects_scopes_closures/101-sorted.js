#!/usr/bin/node
const { dict } = require('./101-data');
const NewDict = {};

for (const userId in dict) {
  const occurance = dict[userId];
  if (!(occurance in NewDict)) {
    NewDict[occurance] = [];
  }
  NewDict[occurance].push(userId);
}
console.log(NewDict);
