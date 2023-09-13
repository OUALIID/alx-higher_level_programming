#!/usr/bin/node

function factorial (number) {
  if (number === 0 || number === 1) {
    return 1;
  }
  return number * factorial(number - 1);
}

const args = process.argv.slice(2);
const number = parseInt(args[0]);
if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
