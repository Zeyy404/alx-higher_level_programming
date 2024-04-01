#!/bin/bash
# makes a request to `0.0.0.0:5000/catch_me` that causes a respond with a message containing `You got me!`
curl -sX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -L | awk -F'<body>|</body>' '{print $2}'
