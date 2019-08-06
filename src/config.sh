DEFAULT_DATA_PATH_EN="/data/data.en"
DEFAULT_DATA_PATH_DE="/data/data.de"
DEFAULT_TRAINING_PATH="/data"

TRAIN_SOURCE_FILE_EN="/train.src.en"
TRAIN_SOURCE_FILE_DE="/train.src.de"
TRAIN_TARGET_FILE_DE="/train.trg.de"
TRAIN_BASE_FILE_DE="/train.base.de"
TRAIN_POS_FILE_DE="/train.pos.de"

VAL_SOURCE_FILE_EN="/validation.src.en"
VAL_SOURCE_FILE_DE="/validation.src.de"
VAL_TARGET_FILE_DE="/validation.trg.de"
VAL_BASE_FILE_DE="/validation.base.de"
VAL_POS_FILE_DE="/validation.pos.de"
VAL_OUTPUT_DE="validation.de.output"

TEST_SOURCE_FILE_EN="/test.src.en"
TEST_SOURCE_FILE_DE="/test.src.de"
TEST_TARGET_FILE_DE="/test.trg.de"
TEST_BASE_FILE_DE="/test.base.de"
TEST_OUTPUT_FILE_DE="/test.trg.de.output"
TEST_POS_FILE_DE="/test.pos.de.output"
RESULT_FILE_DE="/result.de"

DEFAULT_EVAL_SOURCE_PATH="/data/test.trg.de.output_one_word"
DEFAULT_EVAL_TARGET_PATH="/data/test.trg.de"
DEFAULT_SCORING_FILE="/scoring.output"

PREPROCESS_REMOVE_PUNCTUATION=0
PREPROCESS_REMOVE_NUMBERS=0
PREPROCESS_TRUE_CASER=1
TRUE_CASER_COUNT_FILE="/true_caser_count.en"
SOURCE_DATA_PATH="/source_data"

DEFAULT_EVAL_SOURCE_PATH="/data/test.trg.de.output_one_word"
DEFAULT_EVAL_TARGET_PATH="/data/test.trg.de"
DEFAULT_SCORING_FILE="/scoring.output"
DEFAULT_LOW_BOUND_SCORING_FILE="/lowerbound-scoring.output"

DEFAULT_MOST_COMMON_LIST_DE="/german-word-list-total.csv"
DEFAULT_MOST_COMMON_PATH="$DEFAULT_TRAINING_PATH/no_most_common"  # scoring, when most common words are ignored
DEFAULT_POS_PATH="$DEFAULT_TRAINING_PATH/only_noun"  # scoring, when only nouns are considered
DEFAULT_POS_LIST="NOUN" # POS considered for the POS-scoring --> see https://spacy.io for POS-definition

MOST_COMMON_NUMBER=500
VALIDATION_FRACTION_PERCENTAGE=0.025
TEST_FRACTION_PERCENTAGE=0.10