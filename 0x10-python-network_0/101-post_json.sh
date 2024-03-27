#!/bin/bash
# sends a JSON POST request to a URL and displays the body of the response.
curl -sX POST -d "$(cat $2)" -H "Content-Type: application/json" "$1"
