#!/usr/bin/env bash

cat $1 \
    | sed 's/\@\@ //g' \
    | ../../tools/moses-scripts/scripts/recaser/detruecase.perl \
    | ../../tools/moses-scripts/scripts/tokenizer/detokenize.perl -l ro \
    | ../../tools/moses-scripts/scripts/generic/multi-bleu-detok.perl ../../data/validation.trg.de \
    | sed -r 's/BLEU = ([0-9.]+),.*/\1/'