#!/bin/bash
# sends a GET request with specific header to the URL, and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
