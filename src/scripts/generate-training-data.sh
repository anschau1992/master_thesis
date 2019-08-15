#!/usr/bin/env bash
source ../config.sh
export $(cut -d= -f1 ../config.sh)

# set parent folder as starting point
mydir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
cd ${mydir}
source ./shell-logger.sh

# Pre-process training data
cd ../../src
#shell-log "generate" "Ubuntu: Preprocess Training Data"
#python3 ./__init_generator__.py -vv -ien /source_data/ubuntu/Ubuntu.de-en.en -ide /source_data/ubuntu/Ubuntu.de-en.de -o /data
#shell-log "generate" "OpenOffice: Preprocess Training Data"
#python3 ./__init_generator__.py -vv -ien /source_data/oo/OpenOffice.de-en_GB.en_GB -ide /source_data/oo/OpenOffice.de-en_GB.de -o /data
#shell-log "generate" "PHP: Preprocess Training Data"
#python3 ./__init_generator__.py -vv -ien /source_data/php/PHP.de-en.en -ide /source_data/php/PHP.de-en.de -o /data
#shell-log "generate" "AutoDesk: Preprocess Training Data"
#python3 ./__init_generator__.py -vv -ien /source_data/autodesk.output.en -ide /source_data/autodesk.output.de -o /data
#shell-log "generate" "ParaCrawl: Preprocess additional Training Data without adding to Test and Validation"
#python3 ./__init_generator__.py -vv -ien /source_data/paracrawl/ParaCrawl.de-en.en -ide /source_data/paracrawl/ParaCrawl.de-en.de -o /data -pv 0 -pt 0

# Sampling data TODO: parametrize between over- undersampling
# python3 ./__init_oversampling__.py -vv
sampling="undersampling"
python3 ./__init_undersampling__.py -vv
# shuffle train.tuple
train_tuple=../data/train.tuple
shuf -o ${train_tuple} < ${train_tuple}

# split back into moses files
mkdir -p ../data/${sampling}
touch ../data/${sampling}/train.src.en
touch ../data/${sampling}/train.src.de
touch ../data/${sampling}/train.trg.de
touch ../data/${sampling}/train.src.en
touch ../data/${sampling}/train.base.de
touch ../data/${sampling}/train.pos.de
shell-log "generate" "${sampling}: Split train.tuple into different files"
while read line
do
    IFS='#' read -ra tuple_array <<< ${line}
    echo ${tuple_array[0]} >> ../data/${sampling}/train.src.en
    echo ${tuple_array[1]} >> ../data/${sampling}/train.src.de
    echo ${tuple_array[2]} >> ../data/${sampling}/train.trg.de
    echo ${tuple_array[3]} >> ../data/${sampling}/train.base.de
    echo ${tuple_array[4]} >> ../data/${sampling}/train.pos.de
done < ${train_tuple}
shell-log "generate" "${sampling}: Finished splitting train.tuple"

shell-log "generate" "Clean up"
##rm -rf ../data/${sampling}_data/
##rm -r ../source_data
##rm ../deu.mt