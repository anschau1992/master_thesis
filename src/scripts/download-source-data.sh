#!/usr/bin/env bash
source ./scripts/shell-logger.sh

# Download and unzip the three corpia Ubuntu, OpenOffice and PHP from 'http://opus.nlpl.eu'
# Prepare and pre-process data, merge all three corpia together with the local data from Autodesk (deu.mt.bz2).


mkdir -p ../source_data
cd ../source_data

# get the three corpia
log "download" "Downloading the corpia"
wget -nc --output-document=ubuntu-de-en.txt.zip http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/de-en.txt.zip
wget -nc --output-document=oo-de-en.txt.zip http://opus.nlpl.eu/download.php?f=OpenOffice/v3/moses/de-en_GB.txt.zip
wget -nc --output-document=php-de-en.txt.zip http://opus.nlpl.eu/download.php?f=PHP/v1/moses/de-en.txt.zip

unzip -o ubuntu-de-en.txt.zip -d ./ubuntu
unzip -o oo-de-en.txt.zip -d ./oo
unzip -o php-de-en.txt.zip -d ./php

log "download" "Preprocess the Autodesk source data"
# unzip and pre-process Autodesk data
bzip2 -dk ../deu.mt.bz2
sed -i -e 's//$/g' ../deu.mt # replace multi-char symbol by single char, as 'cut' only works with it
while read line
do
    A="$(cut -d'$' -f1 <<<"$line")"
    B="$(cut -d'$' -f3 <<<"$line")"
    echo "$A" >> autodesk.output.en
    echo "$B" >> autodesk.output.de
done < "../deu.mt"

# Pre-process training data
cd ../src
log "download" "Ubuntu: Preprocess Training Data"
python3 __init_generator__.py -vv -ien ../source_data/ubuntu/Ubuntu.de-en.en -ide ../source_data/ubuntu/Ubuntu.de-en.de -o ./data
log "download" "OpenOffice: Preprocess Training Data"
python3 __init_generator__.py -vv -ien ../source_data/oo/OpenOffice.de-en_GB.en_GB -ide ../source_data/oo/OpenOffice.de-en_GB.de -o ./data
log "download" "PHP: Preprocess Training Data"
python3 __init_generator__.py -vv -ien ../source_data/php/PHP.de-en.en -ide ../source_data/php/PHP.de-en.de -o ./data
log "download" "AutoDesk: Preprocess Training Data"
python3 __init_generator__.py -vv -ien ../source_data/autodesk.output.en -ide ../source_data/autodesk.output.de -o ./data

log "download" "Clean up"
cd ..
rm -r source_data
rm ./deu.mt
