#!/usr/bin/env bash
source ./scripts/shell-logger.sh

MARIAN=${MARIAN_PATH}

# logging method


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
log "config" "Using GPUs: ${GPUS}"

WORKSPACE=8500
N=4
EPOCHS=5
B=12

if [[ ! -e $MARIAN_TRAIN ]]
then
    log "config" "marian is not installed in $MARIAN, you need to compile the toolkit first"
    exit 1
fi

#if [[ ! -e ../tools/moses-scripts ]] || [[ ! -e ../tools/subword-nmt ]] || [[ ! -e ../tools/sacreBLEU ]]
if [[ ! -e ../tools/moses-scripts ]]
then
    log "config" "missing tools in ../tools, you need to download them first"
    exit 1
fi

mkdir -p ../model



if [[ ! -e "../data/train.src.en" ]] || [[ ! -e "../data/train.src.de" ]] || [[ ! -e "../data/train.trg.de" ]]
then
    # delete potential old training data
    rm -r -f ../data
    log "data" "missing training data. Will be downloaded and prepared..."
    ./scripts/download-source-data.sh
else
    log "data" "Found generated training data under '../data'"
fi

## create common vocabulary
#if [[ ! -e "../model/vocab.deen.yml" ]]
#then
#    cat ../data/train.src.de ../data/train.src.en | ${MARIAN_VOCAB} --max-size 36000 > ../model/vocab.deen.yml
#fi

# train model
mkdir -p ../model

log "train" "Start Model Training"
${MARIAN_TRAIN} \
    --model ../model/model.npz --type multi-transformer \
    --train-sets ../data/train.src.en ../data/train.src.de  ../data/train.trg.de\
    --max-length 100 \
    --mini-batch-fit -w 6000 --maxi-batch 1000 \
    --valid-freq 5000 --save-freq 5000 --disp-freq 500 \
    --valid-metrics ce-mean-words perplexity\
    --valid-translation-output ../data/validation.de.output \
    --valid-sets ../data/validation.src.en ../data/validation.src.de ../data/validation.trg.de \
    --valid-mini-batch 64 \
    --beam-size 12 --normalize=0 \
    --overwrite --keep-best \
    --vocabs ../model/vocab.deen.spm ../model/vocab.deen.spm ../model/vocab.deen.spm \
    --dim-vocabs 32000 32000 32000 \
    --early-stopping 10 --after-epochs 10 --cost-type=ce-mean-words \
    --log ../model/train.log --valid-log ../model/valid.log \
    --enc-depth 6 --dec-depth 6 \
    --tied-embeddings \
    --transformer-dropout 0.1 --label-smoothing 0.1 \
    --learn-rate 0.00003 --lr-warmup 32000 --lr-decay-inv-sqrt 16000 --lr-report \
    --optimizer-params 0.9 0.98 1e-09 --clip-norm 5 \
    --devices ${GPUS} --seed 1111 \
    --exponential-smoothing


# Testing phase
if [[ ! -e "../data/test.trg.de.output" ]]
then
    log "test" "Start of Testing"
    touch ../data/test.trg.de.output
    ${MARIAN_DECODER} \
        -m ../model/model.npz \
        -i ../data/test.src.en ../data/test.src.de \
        -b 6 --normalize=0 -w 2000 -d ${GPUS} \
        --mini-batch 64 --maxi-batch 100 --maxi-batch-sort src \
        --vocabs ../model/vocab.deen.spm ../model/vocab.deen.spm ../model/vocab.deen.spm \
        --output ../data/test.trg.de.output \
        --log ../model/test.log \
        --max-length-factor 0.3 \
        --word-penalty 10

    # make file with only one word TODO: find better way -> model should actually do this itself
    python3 crop-to-first-word.py

else
    log "train" "Testing already done; Skip it"
fi

# Calculates the score if no flectation, but
log "score" "Calculate Lower bound"
touch ../data/lowerbound-score.output
python3 __init_evaluators__.py -s ../data/test.src.de -t ../data/test.trg.de -o ../data/lowerbound-score.output -vv

log "score" "Calculate Score"
touch ../data/scoring.output
python3 __init_evaluators__.py -vv

