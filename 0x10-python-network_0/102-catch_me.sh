#!/bin/bash
# makes a request to `0.0.0.0:5000/catch_me` that causes a respond with a message containing `You got me!`
curl -sX PUT -L -d "user_id=98" -H "Origin:CatchMeIfYouCan" "0.0.0.0:5000/catch_me"
