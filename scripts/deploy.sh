#!/bin/bash

git pull origin master
sudo docker-compose up -d --build
