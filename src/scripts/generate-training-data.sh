#!/usr/bin/env bash
source ../config.sh
export $(cut -d= -f1 ../config.sh)

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

# Evaluate mode
sampling_mode=""
if [${SAMPLING_MODE} == 'oversampling']; then
    sampling_mode="/oversampling"
    python3 ./__init_oversampling__.py -vv
elif [${SAMPLING_MODE} == 'undersampling']; then
    sampling_mode="/undersampling"
    python3 ./__init_undersampling__.py -vv
fi

if  [${sampling_mode} != '']; then

    # shuffle train.tuple
    train_tuple=../data/train.tuple
    shuf -o ${train_tuple} < ${train_tuple}

    # split back into moses files
    mkdir -p ../data${sampling_mode}
    touch ../data${sampling_mode}/train.src.en
    touch ../data${sampling_mode}/train.src.de
    touch ../data${sampling_mode}/train.trg.de
    touch ../data${sampling_mode}/train.src.en
    touch ../data${sampling_mode}/train.base.de
    touch ../data${sampling_mode}/train.pos.de
    shell-log "generate" "${sampling_mode}: Split train.tuple into different files"
    while read line
    do
        IFS='#' read -ra tuple_array <<< ${line}
        echo ${tuple_array[0]} >> ../data${sampling_mode}/train.src.en
        echo ${tuple_array[1]} >> ../data${sampling_mode}/train.src.de
        echo ${tuple_array[2]} >> ../data${sampling_mode}/train.trg.de
        echo ${tuple_array[3]} >> ../data${sampling_mode}/train.base.de
        echo ${tuple_array[4]} >> ../data${sampling_mode}/train.pos.de
    done < ${train_tuple}
    shell-log "generate" "${sampling_mode}: Finished splitting train.tuple"
    rm -rf ../data${sampling_mode}_data/
fi

shell-log "generate" "Clean up"
rm -r ../source_data
rm ../deu.mt