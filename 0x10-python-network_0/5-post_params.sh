#!/bin/bash
# A Bash script that takes a URL, sends a POST request to the URL passed, and displays the response body.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
