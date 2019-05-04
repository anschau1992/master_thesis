#!/usr/bin/env bash

MARIAN=../software/marian/build

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

if [[ ! -e ../tools/moses-scripts ]] || [[ ! -e ../tools/subword-nmt ]] || [[ ! -e ../tools/sacreBLEU ]]
then
    echo "missing tools in ../tools, you need to download them first"
    exit 1
fi

mkdir -p model


if [[ ! -e "training/train.src.en" ]]
then
    echo "missing train.src.en in ./training, you need to have training data first"
fi

if [[ ! -e "training/train.src.de" ]]
then
    echo "missing train.src.de in ./training, you need to have training data first"
fi

if [[ ! -e "training/train.trg.de" ]]
then
    echo "missing train.trg.de in ./training, you need to have training data first"
fi

# create common vocabulary
if [[ ! -e "model/vocab.ende.yml" ]]
then
    cat data/corpus.bpe.en data/corpus.bpe.de | ${MARIAN_VOCAB} --max-size 36000 > model/vocab.ende.yml
fi

# train model
mkdir -p model.back
if [[ ! -e "model.back/model.npz.best-translation.npz" ]]
then
    ${MARIAN_TRAIN} \
        --model model.back/model.npz --type s2s \
        --train-sets data/corpus.bpe.de data/corpus.bpe.en \
        --max-length 100 \
        --vocabs model/vocab.ende.yml model/vocab.ende.yml \
        --mini-batch-fit -w 3500 --maxi-batch 1000 \
        --valid-freq 10000 --save-freq 10000 --disp-freq 1000 \
        --valid-metrics ce-mean-words perplexity translation \
        --valid-script-path "bash ./scripts/validate.en.sh" \
        --valid-translation-output data/valid.bpe.de.output --quiet-translation \
        --valid-sets data/valid.bpe.de data/valid.bpe.en \
        --valid-mini-batch 64 --beam-size 12 --normalize=1 \
        --overwrite --keep-best \
        --early-stopping 5 --after-epochs 10 --cost-type=ce-mean-words \
        --log model.back/train.log --valid-log model.back/valid.log \
        --tied-embeddings-all --layer-normalization \
        --devices $GPUS --seed 1111 \
        --exponential-smoothing
