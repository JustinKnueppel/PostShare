#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR
DATE_STRING=$(date +'%Y-%m-%d')
mkdir -p logs
LOGFILE="logs/$DATE_STRING.log"
touch $LOGFILE
docker build . -t post-share && docker run post-share > $LOGFILE 2>&1
