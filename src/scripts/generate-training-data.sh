#!/usr/bin/env bash

# set parent folder as starting point
mydir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
cd ${mydir}
source ./shell-logger.sh

# Pre-process training data
cd ../../src
shell-log "generate" "Ubuntu: Preprocess Training Data"
python3 ./__init_generator__.py -vv -ien /source_data/ubuntu/Ubuntu.de-en.en -ide /source_data/ubuntu/Ubuntu.de-en.de -o /data
shell-log "generate" "OpenOffice: Preprocess Training Data"
python3 ./__init_generator__.py -vv -ien /source_data/oo/OpenOffice.de-en_GB.en_GB -ide /source_data/oo/OpenOffice.de-en_GB.de -o /data
shell-log "generate" "PHP: Preprocess Training Data"
python3 ./__init_generator__.py -vv -ien /source_data/php/PHP.de-en.en -ide /source_data/php/PHP.de-en.de -o /data
shell-log "generate" "AutoDesk: Preprocess Training Data"
python3 ./__init_generator__.py -vv -ien /source_data/autodesk.output.en -ide /source_data/autodesk.output.de -o /data
shell-log "generate" "ParaCrawl: Preprocess additional Training Data without adding to Test and Validation"
python3 ./__init_generator__.py -vv -ien /source_data/paracrawl/ParaCrawl.de-en.en -ide /source_data/paracrawl/ParaCrawl.de-en.de -o /data -pv 0 -pt 0

log "generate" "Clean up"
rm -r ../source_data
rm ../deu.mt