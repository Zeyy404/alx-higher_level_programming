#!/bin/bash
# makes a request to `0.0.0.0:5000/catch_me` that causes a respond with a message containing `You got me!`
curl -sX PUT -d "You got me!" -H "User-Agent: CatchMeIfYouCan" 0.0.0.0:5000/catch_me
