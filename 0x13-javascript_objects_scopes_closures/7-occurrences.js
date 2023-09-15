#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let count = 0;
  for (const i of list) {
    if (i === searchElement) {
      count += 1;
    }
  }
  return (count);
}
module.exports = { nbOccurences };
