#!/bin/bash
# A Bash script that takes a URL and displays all the HTTP methods that the server will accept.
# curl -s -i -X OPTIONS "$1" | awk '/Allow:/ {print $2}'
curl -s -i -X OPTIONS "$1" | awk -F ': ' '/Allow:/ {print $2}'
