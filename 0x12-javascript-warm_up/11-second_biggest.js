#!/usr/bin/node

const args = process.argv.slice(2);
let largest = -Infinity;
let secondLargest = -Infinity;
for (const i of args) {
  const number = parseInt(i);
  if (number > largest) {
    secondLargest = largest;
    largest = number;
  } else if (number > secondLargest && number !== largest) {
    secondLargest = number;
  }
}
console.log(secondLargest);
