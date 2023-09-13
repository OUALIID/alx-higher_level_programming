#!/usr/bin/node

const args = process.argv.slice(2);
const a = parseInt(args[0]);
const b = parseInt(args[1]);
function add (a, b) {
  return a + b;
}
if (args.length === 0 || args.length === 1 || isNaN(add(a, b))) {
  console.log('NaN');
} else {
  if (isNaN(add(a, b))) {
    console.log('NaN');
  } else {
    console.log(add(a, b));
  }
}
