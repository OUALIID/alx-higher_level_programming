#!/bin/bash
# A Bash script makes a request to 0.0.0.0:5000/catch_me causing the server to respond with a message containing You've got me!
curl -sX POST -H "Content-Type: application/json" --data "@$2" "$1"
