#!/bin/bash

# build rpg docker image
docker build -t rpg .

# run rpg docker container
docker run -d -p 5555:5555 rpg

# check docker info
docker ps
