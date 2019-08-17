##
## Downloads the different source data and prepares them for data generation.
##
#!/usr/bin/env bash


# set parent folder as starting point
mydir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
cd ${mydir}
source ./shell-logger.sh

# Download and unzip the three corpia Ubuntu, OpenOffice and PHP from 'http://opus.nlpl.eu'
# Prepare and pre-process data, merge all three corpia together with the local data from Autodesk (deu.mt.bz2).
mkdir -p ../../source_data
cd ../../source_data

# get the corpia
shell-log "download" "Downloading the corpia"
wget -nc --output-document=ubuntu-de-en.txt.zip http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/de-en.txt.zip
wget -nc --output-document=oo-de-en.txt.zip http://opus.nlpl.eu/download.php?f=OpenOffice/v3/moses/de-en_GB.txt.zip
wget -nc --output-document=php-de-en.txt.zip http://opus.nlpl.eu/download.php?f=PHP/v1/moses/de-en.txt.zip

shell-log "download" "Downloading the ParaCrawl data"
wget -nc --output-document=paracrawl-de-en.txt.zip http://opus.nlpl.eu/download.php?f=ParaCrawl/v1/moses/de-en.txt.zip

unzip -o ubuntu-de-en.txt.zip -d ./ubuntu
unzip -o oo-de-en.txt.zip -d ./oo
unzip -o php-de-en.txt.zip -d ./php
unzip -o paracrawl-de-en.txt.zip -d ./paracrawl

shell-log "download" "Truncate the ParaCrawl data to 10 Mio lines"
sed -i '10000001,$ d' ./paracrawl/ParaCrawl.de-en.en
sed -i '10000001,$ d' ./paracrawl/ParaCrawl.de-en.de
paraen=`wc -l < ./paracrawl/ParaCrawl.de-en.en | awk '{print $1}'`
parade=`wc -l < ./paracrawl/ParaCrawl.de-en.de | awk '{print $1}'`
shell-log "download" "Length ParaCrlaw.de-en.en: $paraen"
shell-log "download" "Length ParaCrlaw.de-en.de: $parade"


shell-log "download" "Preprocess the Autodesk source data"
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