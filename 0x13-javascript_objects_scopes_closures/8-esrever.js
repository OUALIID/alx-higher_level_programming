#!/usr/bin/node

exports.esrever = function (list) {
  let beginning = 0;
  let end = list.length - 1;

  while (beginning <= end) {
    const tmp = list[beginning];
    list[beginning] = list[end];
    list[end] = tmp;

    beginning++;
    end--;
  }
  return list;
};
