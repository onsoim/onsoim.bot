#!/bin/sh

python3 -u src/main.py >> log/$(date +"%Y-%m-%d").log &

/bin/sh
