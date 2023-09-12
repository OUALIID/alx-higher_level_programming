#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);
if (args.length === 0 || isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
