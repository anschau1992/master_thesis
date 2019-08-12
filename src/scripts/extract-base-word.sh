#!/usr/bin/env bash
##
## Extracts out all lines, where the source token matches exactly the parameter $3.
## IMPORTANT: it is case-sensitive.
##
## $1: folder-name in generated_approaches/ => e.g. 4
## $2: output-file name
## $3: specific base word to consider
## $4: subfolder (optional)

# set parent folder as starting point
mydir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
cd ${mydir}


if [[ -z "$4" ]]
then
   FOLDER=""
else
   FOLDER="/$4"
fi
LINE_LENGTH=$(wc -l < ../../generated_approaches/"$1""$FOLDER"/test.src.de)



printf "Line;Source-DE;Target-DE;Generated-Output;Accuracy;Chrf;Source-EN;Base-DE\\n" > $2
i=0
paste -d ";" "../../generated_approaches/"$1""${FOLDER}"/test.src.de" "../../generated_approaches/"$1""${FOLDER}"/test.trg.de" \
    "../../generated_approaches/"$1""${FOLDER}"/test.trg.de.output" "../../generated_approaches/"$1""${FOLDER}"/scoring.output" \
    "../../generated_approaches/"$1""${FOLDER}"/test.src.en" "../../generated_approaches/"$1""${FOLDER}"/test.base.de" | (
    while read line ; do
        i=$((i+1))
        src_de="$(cut -d';' -f1 <<< ${line})"
        if [[ "$3" == ${src_de} ]]
        then
            printf  "${i};${line}\n">> $2
            echo "Match on line ${i}"
        fi
    done
    )




#printf "Line;Source-DE;Target-DE;Generated-Output;Accuracy;Chrf;Source-EN;Base-DE\\n" > $2
#i=0
#paste -d ";" "../../generated_approaches/"$1""${FOLDER}"/test.src.de" "../../generated_approaches/"$1""${FOLDER}"/test.trg.de" \
#    "../../generated_approaches/"$1""${FOLDER}"/test.trg.de.output" "../../generated_approaches/"$1""${FOLDER}"/scoring.output" \
#    "../../generated_approaches/"$1""${FOLDER}"/test.src.en" "../../generated_approaches/"$1""${FOLDER}"/test.base.de" | (
#    while read src_de trg_de trg_de_output scoring_line src_en base_de ; do
#        i=$((i+1))
#        if [[ "$3" == ${src_de} ]]
#        then
#
#             echo  "${i};${src_de};${trg_de};${trg_de_output};${scoring_line};${src_en//;/ };${base_de}\\n"
#
#        fi
#    done
#    )

#for i in `seq 0 ${LINE_LENGTH}`
#do
#    src_de=$(sed "${i}!d" "../../generated_approaches/"$1""${FOLDER}"/test.src.de")
#
#    if [[ "$3" == ${src_de} ]]
#    then
#
#        trg_de=$(sed "${i}!d" "../../generated_approaches/"$1""${FOLDER}"/test.trg.de")
#        trg_de_output=$(sed "${i}!d" "../../generated_approaches/"$1""${FOLDER}"/test.trg.de.output")
#        src_en=$(sed "${i}!d" "../../generated_approaches/"$1""${FOLDER}"/test.src.en")
#        base_de=$(sed "${i}!d" "../../generated_approaches/"$1""${FOLDER}"/test.base.de")
#
#        scoring_line=$(sed "${i}!d" "../../generated_approaches/"$1""${FOLDER}"/scoring.output")
#        accuracy=( "$(echo ${scoring_line} | cut -d";" -f1)" )
#        chrf=( "$(echo ${scoring_line} | cut -d";" -f2)" )
#
#        printf  "${i};${src_de};${trg_de};${trg_de_output};${accuracy};${chrf};${src_en};${base_de}\\n" >> $2
#        echo "FOUND a match on line ${i}"
#    fi
#done


#            printf  "${i};${src_de};${trg_de};${trg_de_output};${accuracy};${chrf};${src_en};${base_de}\\n" >> $2