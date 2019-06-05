# Clean up after training and testing. Set everything up for a new round of Model-training
#!/usr/bin/env bash

# create new folder for the current approach
i=1
while [[ -d "../generated_approaches/$i" ]]
do
    i=$(( $i + 1))
done
mkdir -p "../generated_approaches/$i"


# move and copy model files
mv ../model/train.log ../generated_approaches/${i}/train.log
mv ../model/valid.log ../generated_approaches/${i}/valid.log
mv ../model/test.log ../generated_approaches/${i}/test.log
mv ../data/scoring.output ../generated_approaches/${i}/scoring.output
mv ../data/lowerbound-score.output ../generated_approaches/${i}/lowerbound-score.output
cp ../src/run-me.sh ../generated_approaches/${i}/run-me.sh

# move and copy test files
mv ../data/test.trg.de.output ../generated_approaches/${i}/test.trg.de.output
cp ../data/test.src.en ../generated_approaches/${i}/test.src.en
cp ../data/test.src.de ../generated_approaches/${i}/test.src.de
cp ../data/test.trg.de ../generated_approaches/${i}/test.trg.de

mv ./run-me.log ../generated_approaches/${i}/run-me.log

# zip all
zip ../generated_approaches/model_${i}.zip ../generated_approaches/${i}/train.log ../generated_approaches/${i}/valid.log \
 ../generated_approaches/${i}/test.log ../generated_approaches/${i}/scoring.output \
  ../generated_approaches/${i}/lowerbound-score.output ../generated_approaches/${i}/run-me.sh \
  ../generated_approaches/${i}/run-me.log

# clean up & set up for new training round
rm -r ../model