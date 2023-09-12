#!/usr/bin/node

const args = process.argv.slice(2);
if (args[0]) {
  const number = parseInt(args[0]);
  if (!isNaN(number)) {
    console.log('My number: ' + args[0]);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
