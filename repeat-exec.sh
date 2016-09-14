#!/bin/bash

if [ $# -eq 0 ]; then
    echo $0: usage: interval command
    exit 1
fi

while true; do ${@:2}; sleep $1; done
