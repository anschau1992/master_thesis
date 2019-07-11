#!/usr/bin/env bash
##
## Print out random lines of the given model to compare the results with the source.
## If strings are not defined '[NULL]' is set into the table.
##
## $1: folder-name in generated_approaches/ => e.g. 4
## $2: number of lines to print

# set parent folder as starting point
mydir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
cd ${mydir}


LINE_LENGTH=$(wc -l < ../../generated_approaches/"$1"/test.src.de)

if [ -z "$3" ]
then
    let "RANDOM_NUMB= $RANDOM % ${LINE_LENGTH}"
else
    RANDOM_NUMB=$3
fi

# Extract data out of files
test_src_de=()
test_trg_de=()
test_trg_de_output=()
test_src_en=()
test_base_de=()
accuracy=()
chrf=()

max_i=$(( ${RANDOM_NUMB}+$2 ))
for i in `seq ${RANDOM_NUMB} ${max_i}`
do
    src_de=$(sed "${i}!d" "../../generated_approaches/"$1"/test.src.de")
    test_src_de+=( "$( [[ -z "$src_de" ]] && echo "[NULL]" || echo ${src_de} )" )

    trg_de=$(sed "${i}!d" "../../generated_approaches/"$1"/test.trg.de")
    test_trg_de+=( "$( [[ -z "$trg_de" ]] && echo "[NULL]" || echo ${trg_de} )" )

    trg_de_output=$(sed "${i}!d" "../../generated_approaches/"$1"/test.trg.de.output")
    test_trg_de_output+=( "$( [[ -z "$trg_de_output" ]] && echo "[NULL]" || echo ${trg_de_output} )" )

    src_en=$(sed "${i}!d" "../../generated_approaches/"$1"/test.src.en")
    test_src_en+=( "$( [[ -z "$src_en" ]] && echo "[NULL]" || echo ${src_en} )" )

    base_de=$(sed "${i}!d" "../../generated_approaches/"$1"/test.base.de")
    test_base_de+=( "$( [[ -z "$base_de" ]] && echo "[NULL]" || echo ${base_de} )" )

    scoring_line=$(sed "${i}!d" "../../generated_approaches/"$1"/scoring.output")
    accuracy+=( "$(echo ${scoring_line} | cut -d";" -f1)" )
    chrf+=( "$(echo ${scoring_line} | cut -d";" -f2)" )
done

# Table formatting
divider=====================================================================
divider=$divider$divider$divider$divider
width=180


header="\n %-10s %-25s %-30s %-30s %-15s %-15s %-20s\n"
formatf=" %-10i %-25s %-30s %-30s %-15i %-15g %.120s\n"
format2=" %-10s %-25s %-30s %-30s %-15s %-15s %.120s\n"
printf "$header" "#Line" "Source-DE" "Target-DE" "Generated-Output" "Accuracy" "Chrf" "Source-EN | Base-DE"
printf "%$width.${width}s\n" "$divider"
for i in `seq 0 $2`
do
    printf "$formatf" \
    $(( ${RANDOM_NUMB}+i )) ${test_src_de[i]} ${test_trg_de[i]} ${test_trg_de_output[i]} ${accuracy[i]} ${chrf[i]} "${test_src_en[i]}"
    printf "$format2" \
    "          " "                         " "                              " "                              " "               " "               " "${test_base_de[i]}"
    printf "$format2" \
    "----------" "-------------------------" "------------------------------" "------------------------------" "---------------" "---------------" "------------------------------"
done