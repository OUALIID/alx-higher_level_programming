#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBase (Number) {
    return Number.toString(base);
  };
};
