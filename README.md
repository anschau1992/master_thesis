# Master thesis - Morphological Inflection of Terminology for Constrained Neural Machine Translation


## Introduction
This is my general repository considering all my work for my master thesis. It consist of:
* Proposal (proposal.zip)
* Project itself:
  * Generator - generates training data out of translation data
  * Predictor (TODO)
  * Evaluator - evaluates the results of the predictor using gold data from the generator

## Prerequisites 
1. Install python 3.7: https://www.python.org/downloads/
2. Install pip3
3. Make sure you have pip installed : https://pip.pypa.io/en/stable/installing/

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
4. Install the depending python libraries: (TODO: überprüfen der benötigten Libraries)
    ```
        pip3 install -r requirements.txt
    ```
5. Install the spaCy models for german language:
    ```
    python3 -m spacy download de
    ```
6. Run the program:
    ```
    cd src
    ./run-me.sh
    ```
## Useful commands
 TODO

## Useful links

- [Neural Monkey - Open toolkit for sequence learning using Tensorflow](https://neural-monkey.readthedocs.io/en/latest/)
- [Marian - Quick start](https://marian-nmt.github.io/quickstart/)
- [Marian - Github repo](https://github.com/marian-nmt/marian)
- [Marian - Transformer](https://github.com/marian-nmt/marian-examples/tree/master/wmt2017-transformer)
- [Opus - open parallel corpus](http://opus.nlpl.eu/)
- [Autodesk - Post-Editing Data Corpus](https://mailman.stanford.edu/pipermail/parser-user/2015-April/003166.html)

## Related Papers

- [Fast Lexically Constrained Decoding with Dynamic Beam Allocation for Neural Machine Translation](https://arxiv.org/abs/1804.06609)
- [Lexically Constrained Decoding for Sequence Generation Using Grid Beam Search](https://arxiv.org/abs/1704.07138)
- [Neural Machine Translation of Rare Words with Subword Units](https://www.aclweb.org/anthology/P16-1162)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [SentencePiece: A simple and language independent subword tokenizer and detoniker for Neural Text Processing](https://arxiv.org/pdf/1808.06226.pdf)
- [CHRF: character n-gram F-score for automatic MT evaluation](http://www.statmt.org/wmt15/pdf/WMT49.pdf)
- [ParaCrawl: a collection of parallel corpora](http://www.lrec-conf.org/proceedings/lrec2012/pdf/463_Paper.pdf) --> cite it if you use ParaCrawl corpora!  
