#!/bin/bash

set -e
set -x

CURRENT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Build container image from Dockerfile
docker build -t gitminer ${CURRENT_PATH}/..

# Copy your Github cookie and set it as an env variable
GITHUB_COOKIE=""

# Run GitMiner image we built earlier
docker run \
    --rm \
    -v ${CURRENT_PATH}:/loot \
    gitminer -m wordpress -q 'filename:shadow' -c ${GITHUB_COOKIE} -o /loot/result.txt

# Explanation:
#   -"-rm"                  : remove/cleanup containers after they stop
#   "-v $PWD:/loot"         : mount current working directory as "/loot" inside the container
#   "gitminer"              : name of the container image we built in previous steps
#   "-m ... -q ... -c ..."  : flags for gitminer are passed into the container
#   "-o /loot/results.txt"  : output results to "/loot" path in container, which in turn makes "result.txt" appear on local host
