#!/bin/bash
response=$(curl -s -w "%{size_download}" -o /dev/null "$1")
echo "$response"
