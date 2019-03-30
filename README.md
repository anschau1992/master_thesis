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
2. Make sure you have pip installed : https://pip.pypa.io/en/stable/installing/

## Setup
1. Start the virtual environment (from root directory of the repo): 

    `` source src/venv/bin/activate``
3. Start the generator:

    `` python3 src/generator.py``
  
## Useful commands
 TODO

## Useful links

- [Neural Monkey - Open toolkit for sequence learning using Tensorflow](https://neural-monkey.readthedocs.io/en/latest/)
- [Marian - Quick start](https://marian-nmt.github.io/quickstart/)
- [Marian - Github repo](https://github.com/marian-nmt/marian)
- [Marian - Transformer](https://github.com/marian-nmt/marian-examples/tree/master/wmt2017-transformer)
- 

## Related Papers

- [Fast Lexically Constrained Decoding with Dynamic Beam Allocation for Neural Machine Translation](https://arxiv.org/abs/1804.06609)
- [Lexically Constrained Decoding for Sequence Generation Using Grid Beam Search](https://arxiv.org/abs/1704.07138)
- [Neural Machine Translation of Rare Words with Subword Units](https://www.aclweb.org/anthology/P16-1162)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)