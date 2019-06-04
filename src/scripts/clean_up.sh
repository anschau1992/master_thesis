# Clean up after training and testing. Set everything up for a new round of Model-training
#!/usr/bin/env bash

# create new folder for the current approach
i=1
while [[ -d "../generated_approaches/$i" ]]
do
    i=$(( $i + 1))
done
mkdir -p "../generated_approaches/$i"


# move and copy files
mv ../model/train.log ../generated_approaches/${i}/train.log
mv ../model/valid.log ../generated_approaches/${i}/valid.log
mv ../model/test.log ../generated_approaches/${i}/test.log
mv ../data/scoring.output ../generated_approaches/${i}/scoring.output
mv ../data/lowerbound-score.output ../generated_approaches/${i}/lowerbound-score.output
cp ../src/run-me.sh ../generated_approaches/${i}/run-me.sh

# clean up & set up for new training round
rm ../data/test.trg.de.output
rm -r ../model