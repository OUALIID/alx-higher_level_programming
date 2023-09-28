#!/bin/bash
# A Bash script that takes a URL, sends a request to the URL, and displays the size of the response body.
curl --silent --head "$1" | grep -i 'content-length' | awk '{print $2}'
