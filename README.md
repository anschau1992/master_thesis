# Master thesis - Morphological Inflection of Terminology for Constrained Neural Machine Translation


## Introduction
Recently proposed constrained decoding approaches
 allow the inclusion of pre-defined terms in neural machine translation output.
  Even though neural machine translation systems generally achieve remarkable translation quality,
   the appropriate inflection of these terms is an open problem: their base form is placed without
    any modification in the output, which may lead to grammatically incorrect results.
     We examine the use of a stand-alone sequence-to-sequence model to predict the correct inflected form
      of a term given its base form and the source sentence. We show that good results can be achieved in
       terms of overall accuracy, and that the method has limited success in handling rare word forms.

## Prerequisites 
1. Install python 3.7: https://www.python.org/downloads/
2. Install pip3
3. Install MARIAN-NMT with SequencPiece according to its [Setup](https://marian-nmt.github.io/docs/)

## Setup
1. Clone the repository
2. Set the environment variable 'MARIAN_PATH' to the build-path. E.g. put the following into file '.zshrc' or '.bash_profile':
    ```
    export MARIAN_PATH=/home/user/{username}/software/marian/build
    ```
3. Install the marian tools required:
    ```
    cd master-thesis/tools
    make
    ```
4. Install the depending python libraries:
    ```
        pip3 install -r requirements.txt
    ```
5. Install the spaCy models for german language:
    ```
    python3 -m spacy download de
    ```
6. Download the AutoDesk corpus manually from [here](http://www.islrn.org/resources/identify_islrn/). ISLRN is 290-859-676-529-5

7. Run the program (e.g. 1 2 3 for \[GPUS\]):
    ```
    cd src
    ./run-me.sh [GPUS]
    ```

## Useful links

- [Neural Monkey - Open toolkit for sequence learning using Tensorflow](https://neural-monkey.readthedocs.io/en/latest/)
- [Marian - Quick start](https://marian-nmt.github.io/quickstart/)
- [Marian - Github repo](https://github.com/marian-nmt/marian)
- [Marian - Transformer](https://github.com/marian-nmt/marian-examples/tree/master/wmt2017-transformer)
- [Opus - open parallel corpus](http://opus.nlpl.eu/)
- [Autodesk - Post-Editing Data Corpus](https://mailman.stanford.edu/pipermail/parser-user/2015-April/003166.html)
- [Sketchengine - the most common words in German](https://www.sketchengine.eu/german-word-list/)
- [Shuffle two files randomly, but the same](https://www.unix.com/shell-programming-and-scripting/166398-randomly-shuffle-two-text-files-same-way.html)
## Related Papers

- [Fast Lexically Constrained Decoding with Dynamic Beam Allocation for Neural Machine Translation](https://arxiv.org/abs/1804.06609)
- [Lexically Constrained Decoding for Sequence Generation Using Grid Beam Search](https://arxiv.org/abs/1704.07138)
- [Neural Machine Translation of Rare Words with Subword Units](https://www.aclweb.org/anthology/P16-1162)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [SentencePiece: A simple and language independent subword tokenizer and detoniker for Neural Text Processing](https://arxiv.org/pdf/1808.06226.pdf)
- [CHRF: character n-gram F-score for automatic MT evaluation](http://www.statmt.org/wmt15/pdf/WMT49.pdf)
- [ParaCrawl: a collection of parallel corpora](http://www.lrec-conf.org/proceedings/lrec2012/pdf/463_Paper.pdf)
