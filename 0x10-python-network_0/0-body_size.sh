#!/bin/bash

# 0-body_size.sh
#
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes.
#

url="$1"

if [[ -z "$url" ]]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

size=$(curl -s -o /dev/null -w "%{size_download}" "$url")

if [[ "$size" == "0" ]]; then
  echo "Size of the body of the response in bytes: 0"
else
  echo "Size of the body of the response in bytes: $size"
fi

exit 0
