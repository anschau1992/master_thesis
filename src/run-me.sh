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

# train model
mkdir -p ../model/back

echo "Start of Model Training"
${MARIAN_TRAIN} \
    --model ../model/back/model.npz --type multi-transformer \
    --train-sets ../data/train.src.en ../data/train.src.de  ../data/train.trg.de\
    --max-length 100 \
    --mini-batch-fit -w 5000 --maxi-batch 1000 \
    --valid-freq 5000 --save-freq 5000 --disp-freq 500 \
    --valid-metrics ce-mean-words perplexity\
    --valid-translation-output ../data/validation.de.output \
    --valid-sets ../data/validation.src.en ../data/validation.src.de ../data/validation.trg.de \
    --valid-mini-batch 64 \
    --beam-size 12 --normalize=1 \
    --overwrite --keep-best \
    --early-stopping 10 --after-epochs 10 --cost-type=ce-mean-words \
    --log ../model/back/train.log --valid-log ../model/back/valid.log \
    --enc-depth 6 --dec-depth 6 \
    --tied-embeddings \
    --transformer-dropout 0.1 --label-smoothing 0.1 \
    --learn-rate 0.0003 --lr-warmup 16000 --lr-decay-inv-sqrt 16000 --lr-report \
    --optimizer-params 0.9 0.98 1e-09 --clip-norm 5 \
    --devices ${GPUS} --seed 1111 \
    --exponential-smoothing


# inflect test set
echo "Start of Testing"

touch ../data/test.trg.de.output

   #  -c ../model/back/model.npz.best-translation.npz.decoder.yml \
$MARIAN_DECODER \
    -m ../model/back/model.npz \
    -i ../data/test.src.en ../data/test.src.de \
    -b 6 --normalize=1 -w 2000 -d ${GPUS} \
    --mini-batch 64 --maxi-batch 100 --maxi-batch-sort src \
    --vocabs ../data/train.src.en.yml ../data/train.src.de.yml ../data/train.trg.de.yml \
    --output ../data/test.trg.de.output \
    --log ../model/test.log \
    --max-length-factor 0.1 \
    --max-length 15 \
    --word-penalty 10

# calculate scores
echo "Start of Score calculation"
python3 __init_evaluators__.py --vv

