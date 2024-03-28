#!/bin/bash
# This script takes a URL as input, sends a request to that URL, and displays the size of the body of the response in bytes.

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Validate URL format
url="$1"
if [[ ! $url =~ ^https?:// ]]; then
    echo "Error: Invalid URL format. URL must start with 'http://' or 'https://'."
    exit 1
fi

# Send request to the URL and display the size of the body of the response in bytes
response=$(curl -s "$url")
curl_exit_status=$?
if [ $curl_exit_status -ne 0 ]; then
    echo "Error: Failed to retrieve URL. Curl exited with status $curl_exit_status."
    exit 1
fi

echo "$response" | wc -c

# Next
