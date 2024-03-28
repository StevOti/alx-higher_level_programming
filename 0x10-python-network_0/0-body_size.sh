#!/bin/bash
# This script takes a URL as input, sends a request to that URL, and displays the size of the body of the response in bytes.

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and display the size of the body of the response in bytes
curl -s "$1" | wc -c
