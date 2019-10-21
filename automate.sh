#!/bin/bash
date > ~/log.txt
echo '' >> ./output.txt
echo `date` >> ./output.txt
/home/justin/Coding/PostShare/env/bin/python /home/justin/Coding/PostShare/ShareReddit.py 2>> /home/justin/Coding/PostShare/output.txt

