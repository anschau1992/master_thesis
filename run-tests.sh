#!/usr/bin/env bash

## import config variables
source src/config.sh
export $(cut -d= -f1 src/config.sh)

python3 -m unittest discover tests