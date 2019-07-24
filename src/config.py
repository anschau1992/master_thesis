TRAIN_SOURCE_FILE_EN = '/train.src.en'
TRAIN_SOURCE_FILE_DE = '/train.src.de'
TRAIN_TARGET_FILE_DE = '/train.trg.de'
TRAIN_BASE_FILE_DE = '/train.base.de'

VAL_SOURCE_FILE_EN = '/validation.src.en'
VAL_SOURCE_FILE_DE = '/validation.src.de'
VAL_TARGET_FILE_DE = '/validation.trg.de'
VAL_BASE_FILE_DE = '/validation.base.de'

TEST_SOURCE_FILE_EN = '/test.src.en'
TEST_SOURCE_FILE_DE = '/test.src.de'
TEST_TARGET_FILE_DE = '/test.trg.de'
TEST_BASE_FILE_DE = '/test.base.de'
TEST_OUTPUT_FILE_DE = '/test.trg.de.output'

RESULT_FILE_DE = '/result.de'

DEFAULT_DATA_PATH_EN = "/data/data.en"
DEFAULT_DATA_PATH_DE = "/data/data.de"
DEFAULT_TRAINING_PATH = "/data"

DEFAULT_EVAL_SOURCE_PATH = "/data/test.trg.de.output_one_word"
DEFAULT_EVAL_TARGET_PATH = "/data/test.trg.de"
DEFAULT_SCORING_PATH = "/data/scoring.output"

# Preprocessing configurations
PREPROCESS_REMOVE_PUNCTUATION = False
PREPROCESS_REMOVE_NUMBERS = False
PREPROCESS_TRUE_CASER = True
TRUE_CASER_COUNT_FILE = "/true_caser_count.en"
SOURCE_DATA_PATH = "/source_data"


DEFAULT_EVAL_SOURCE_PATH = "/data/test.trg.de.output_one_word"
DEFAULT_EVAL_TARGET_PATH = "/data/test.trg.de"
DEFAULT_SCORING_PATH = "/data/scoring.output"

DEFAULT_MOST_COMMON_LIST_DE = "/german-word-list-total.csv"
DEFAULT_MOST_COMMON_PATH = DEFAULT_TRAINING_PATH + "/no_most_common"

MOST_COMMON_NUMBER = 500
VALIDATION_FRACTION_PERCENTAGE = 0.025
TEST_FRACTION_PERCENTAGE = 0.10