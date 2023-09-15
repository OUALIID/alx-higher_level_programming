#!/usr/bin/node

let Number = 0;

exports.logMe = function (item) {
  console.log(Number + ':' + item);
  Number++;
};
