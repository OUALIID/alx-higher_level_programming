#!/usr/bin/node
const request = require('request');
const url = process.argv.slice(2);
request(url[0], (err, response) => {
    if (err) {
        return;
    }
    console.log(response.userId)
})