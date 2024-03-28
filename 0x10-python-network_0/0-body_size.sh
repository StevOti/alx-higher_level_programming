#!/bin/bash

# This script takes a URL as input, sends a request to that URL, and displays the size of the body of the response in bytes.

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a HEAD request to the URL and print the size of the response body in bytes
curl -sI "$1" | grep -i "content-length:" | cut -d " " -f2
