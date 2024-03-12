#!/usr/bin/node
exports.add_me_maybe = function (number, theFunction) {
  theFunction(++number);
};
