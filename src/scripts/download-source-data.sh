#!/usr/bin/env bash

# Download and unzip the three corpia Ubuntu, OpenOffice and PHP from 'http://opus.nlpl.eu'

cd ..
mkdir -p source_data
cd source_data

# get the three corpia
wget -nc --output-document=ubuntu-de-en.txt.zip http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/de-en.txt.zip
wget -nc --output-document=oo-de-en.txt.zip http://opus.nlpl.eu/download.php?f=OpenOffice/v3/moses/de-en_GB.txt.zip
wget -nc --output-document=php-de-en.txt.zip http://opus.nlpl.eu/download.php?f=PHP/v1/moses/de-en.txt.zip

unzip -o de-en.txt.zip -d ../source_data/ubuntu
unzip -o oo-de-en.txt.zip -d ../source_data/oo
unzip -o php-de-en.txt.zip -d ../source_data/php

# clean
rm -r ubuntu-de-en.txt.zip oo-de-en.txt.zip php-de-en.txt.zip