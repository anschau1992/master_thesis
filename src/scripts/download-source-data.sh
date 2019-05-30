#!/usr/bin/env bash

# Download and unzip the three corpia Ubuntu, OpenOffice and PHP from 'http://opus.nlpl.eu'
# Prepare and preprocess data, merge all three corpia together

cd ..
mkdir -p source_data
cd source_data

# get the three corpia
wget -nc --output-document=ubuntu-de-en.txt.zip http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/de-en.txt.zip
wget -nc --output-document=oo-de-en.txt.zip http://opus.nlpl.eu/download.php?f=OpenOffice/v3/moses/de-en_GB.txt.zip
wget -nc --output-document=php-de-en.txt.zip http://opus.nlpl.eu/download.php?f=PHP/v1/moses/de-en.txt.zip
wget -nc --output-document=ted-de-en.txt.zip http://opus.nlpl.eu/download.php?f=TED2013/v1.1/moses/de-en.txt.zip

unzip -o ubuntu-de-en.txt.zip -d ../source_data/ubuntu
unzip -o oo-de-en.txt.zip -d ../source_data/oo
unzip -o php-de-en.txt.zip -d ../source_data/php
unzip -o ted-de-en.txt.zip -d ../source_data/ted

# Preprocess training data
cd ../src
python3 __init_generator__.py -vv -ien ../source_data/ubuntu/Ubuntu.de-en.en -ide ../source_data/ubuntu/Ubuntu.de-en.de -o ./data
python3 __init_generator__.py -vv -ien ../source_data/oo/OpenOffice.de-en_GB.en_GB -ide ../source_data/oo/OpenOffice.de-en_GB.de -o ./data
python3 __init_generator__.py -vv -ien ../source_data/php/PHP.de-en.en -ide ../source_data/php/PHP.de-en.de -o ./data
python3 __init_generator__.py -vv -ien ../source_data/ted/TED2013.de-en.en -ide ../source_data/ted/TED2013.de-en.de -o ./data

cd ..
rm -r -f source_data
