#!/usr/bin/env bash

MARIAN=${MARIAN_PATH}

# if we are in WSL, we need to add '.exe' to the tool names
if [[ -e "/bin/wslpath" ]]
then
    EXT=.exe
fi

MARIAN_TRAIN=$MARIAN/marian$EXT
MARIAN_DECODER=$MARIAN/marian-decoder$EXT
MARIAN_VOCAB=$MARIAN/marian-vocab$EXT
MARIAN_SCORER=$MARIAN/marian-scorer$EXT

# set chosen gpus
GPUS=0
if [[ $# -ne 0 ]]
then
    GPUS=$@
fi
echo Using GPUs: $GPUS

WORKSPACE=8500
N=4
EPOCHS=5
B=12

if [[ ! -e $MARIAN_TRAIN ]]
then
    echo "marian is not installed in $MARIAN, you need to compile the toolkit first"
    exit 1
fi

#if [[ ! -e ../tools/moses-scripts ]] || [[ ! -e ../tools/subword-nmt ]] || [[ ! -e ../tools/sacreBLEU ]]
if [[ ! -e ../tools/moses-scripts ]]
then
    echo "missing tools in ../tools, you need to download them first"
    exit 1
fi

mkdir -p ../model



if [[ ! -e "../data/train.src.en" ]] || [[ ! -e "../data/train.src.de" ]] || [[ ! -e "../data/train.trg.de" ]]
then
    # delete potential old training data
    rm -r -f ../data
    echo "missing training data. Will be downloaded and prepared..."
    ./scripts/download-source-data.sh
else
    echo "Found generated training data under '../data'"
fi

# create common vocabulary
if [[ ! -e "../model/vocab.deen.yml" ]]
then
    cat ../data/train.src.de ../data/train.src.en | ${MARIAN_VOCAB} --max-size 36000 > ../model/vocab.deen.yml
fi

# train model TODO: move on and finish model, but valid-dataset first
#mkdir -p ../model/back
#if [ ! -e "../model/back/model.npz.best-translation.npz" ]
#then
#    $MARIAN_TRAIN \
#        --model ../model/back/model.npz --type s2s \
#        --train-sets ..data/train.src.en ..data/train.src.de \
#        --max-length 200 \
#        --vocabs ../model/vocab.deen.yml ../model/vocab.deen.yml \
#        --mini-batch-fit -w 3500 --maxi-batch 1000 \
#        --valid-freq 5000 --save-freq 5000 --disp-freq 1000 \
#        --valid-metrics bleu translation \





echo $MARIAN
#if [[ ! -e "training/train.src.en" ]]
#then
#    echo "missing train.src.en in ./training, you need to have training data first"
#fi
#
#if [[ ! -e "training/train.src.de" ]]
#then
#    echo "missing train.src.de in ./training, you need to have training data first"
#fi
#
#if [[ ! -e "training/train.trg.de" ]]
#then
#    echo "missing train.trg.de in ./training, you need to have training data first"
#fi
#
## create common vocabulary
#if [[ ! -e "model/vocab.ende.yml" ]]
#then
#    cat data/corpus.bpe.en data/corpus.bpe.de | ${MARIAN_VOCAB} --max-size 36000 > model/vocab.ende.yml
#fi

