#!/usr/bin/env bash
##
## Extracts out random lines of the given model to compare the results with the source.
## Extraction is done into a csv-file
## If strings are not defined '[NULL]' is set into the table.
##
## $1: folder-name in generated_approaches/ => e.g. 4
## $2: number of lines to print
## $3: specific line number (-1 for random number)
## $4: output-file name
## $5: subfolder to consider (e.g. only-noun) (optional)

# set parent folder as starting point
mydir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
cd ${mydir}


if [[ -z "$5" ]]
then
   FOLDER=""
else
   FOLDER="/$5"

LINE_LENGTH=$(wc -l < ../../generated_approaches/"$1""$FOLDER"/test.src.de)
fi

if [[ $3 < 0 ]]
then
    RANDOM_NUMB=($RANDOM % ${LINE_LENGTH})
else
    RANDOM_NUMB=$3
fi

# Extract data out of files
line_numb=()
test_src_de=()
test_trg_de=()
test_trg_de_output=()
test_src_en=()
test_base_de=()
accuracy=()
chrf=()


for i in `seq 0 $2`
do
    RANDOM_NUMB=($RANDOM % ${LINE_LENGTH})
    line_numb+=(${RANDOM_NUMB})
    src_de=$(sed "${RANDOM_NUMB}!d" "../../generated_approaches/"$1""${FOLDER}"/test.src.de")
    test_src_de+=( "$( [[ -z "$src_de" ]] && echo "[NULL]" || echo ${src_de} )" )

    trg_de=$(sed "${RANDOM_NUMB}!d" "../../generated_approaches/"$1""${FOLDER}"/test.trg.de")
    test_trg_de+=( "$( [[ -z "$trg_de" ]] && echo "[NULL]" || echo ${trg_de} )" )

    trg_de_output=$(sed "${RANDOM_NUMB}!d" "../../generated_approaches/"$1""${FOLDER}"/test.trg.de.output")
    test_trg_de_output+=( "$( [[ -z "$trg_de_output" ]] && echo "[NULL]" || echo ${trg_de_output} )" )

    src_en=$(sed "${RANDOM_NUMB}!d" "../../generated_approaches/"$1""${FOLDER}"/test.src.en")
    test_src_en+=( "$( [[ -z "$src_en" ]] && echo "[NULL]" || echo ${src_en} )" )

    base_de=$(sed "${RANDOM_NUMB}!d" "../../generated_approaches/"$1""${FOLDER}"/test.base.de")
    test_base_de+=( "$( [[ -z "$base_de" ]] && echo "[NULL]" || echo ${base_de} )" )

    scoring_line=$(sed "${RANDOM_NUMB}!d" "../../generated_approaches/"$1""${FOLDER}"/scoring.output")
    accuracy+=( "$(echo ${scoring_line} | cut -d";" -f1)" )
    chrf+=( "$(echo ${scoring_line} | cut -d";" -f2)" )
done

printf "Line;Source-DE;Target-DE;Generated-Output;Accuracy;Chrf;Source-EN;Base-DE\\n" > $4

for i in `seq 0 $2`
do
    printf  "${line_numb[i]};${test_src_de[i]};${test_trg_de[i]};${test_trg_de_output[i]};${accuracy[i]};${chrf[i]};${test_src_en[i]};${test_base_de[i]}\\n" >> $4
done