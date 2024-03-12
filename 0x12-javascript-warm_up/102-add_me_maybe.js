#!/usr/bin/node
exports.add_me_maybe = function (number, theFunction) {
    number++;
    theFunction(number);
};
