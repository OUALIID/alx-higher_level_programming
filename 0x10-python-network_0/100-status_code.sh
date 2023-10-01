#!/bin/bash
# A bash script gets request status code. -w to output words.
# -w "%{http_code}": This option tells `curl` to print a specific 
# piece of information after the request is completed. 
curl -s -w %"{http_code}" -o /dev/null "$1"
