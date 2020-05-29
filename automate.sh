#!/bin/bash
DATE_STRING=$(date +'%Y-%m-%d')
mkdir -p logs
LOGFILE="logs/$DATE_STRING.log"
touch $LOGFILE
docker build . -t post-share > $LOGFILE 2>&1
docker run post-share > $LOGFILE 2>&1