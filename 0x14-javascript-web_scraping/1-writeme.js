#!/usr/bin/node
const fs = require('fs');
const file = process.argv.slice(2);
fs.writeFile(file[0], file[1], 'utf-8', (err) => {
  if (err) {
    const error = {
      Error: err,
      errno: err.errno,
      code: err.code,
      syscall: err.syscall,
      path: err.path
    };
    console.error(error);
    return;
  }
});
