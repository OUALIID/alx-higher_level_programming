#!/bin/bash
# Check if the script has been provided with a URL as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi
body_size=$(curl -s -o /dev/null -w "%{size_download}" -I "$1")

# Display the size of the response body in bytes
echo "$body_size"