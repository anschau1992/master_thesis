import random
import os
import logging


def undersample_data(source_file_en, source_file_de, target_file_de, base_file_de, pos_file_de, dirpath):
    logging.info("Start undersampling.")
    if not os.path.exists(dirpath + "/undersampling_data"):
        os.mkdir(dirpath + "/undersampling_data")

    # TUPLE FILE CREATION
    with open(dirpath + "/train.tuple", 'w+') as train_tuple_file:
        source_file_en.seek(0)
        source_file_de.seek(0)
        target_file_de.seek(0)
        base_file_de.seek(0)
        pos_file_de.seek(0)

        baseword_dicts = {}
        for source_en_line in source_file_en:
            # get next line of other files
            source_en_line = str(source_en_line).replace("#", "*").strip()
            source_de_line = str(next(source_file_de)).replace("#",
                                                               "*").strip()  # assure there is no separator in string
            target_de_line = str(next(target_file_de)).replace("#", "*").strip()
            base_de_line = str(next(base_file_de)).replace("#", "*").strip()
            pos_de_line = str(next(pos_file_de)).replace("#", "*").strip()

            if source_de_line not in baseword_dicts:
                baseword_dicts[source_de_line] = {target_de_line}
            else:
                baseword_dicts[source_de_line].add(target_de_line)

            try:
                with open(dirpath + "/undersampling_data/" + target_de_line + ".tuple", 'a+') as target_tuple_file:
                    target_tuple_file.write(source_en_line + "#" + source_de_line + "#"
                                            + target_de_line + "#" + base_de_line + "#"
                                            + pos_de_line + "\n")
            except Exception as ex:
                print('Too long file name, Skipped')
                continue


        logging.info("Oversampling: Wrote all already existing line into tuple-file as tuples")

        for baseword_dict in baseword_dicts:
            word_forms = baseword_dicts[baseword_dict]
            if len(word_forms) < 2:
                continue
            min_word_form_occurance = 999999999

            for word_form in word_forms:
                word_form_occurance = 0
                with open(dirpath + "/undersampling_data/" + word_form + ".tuple", 'r') as word_form_file:
                    for line in word_form_file:
                        word_form_occurance += 1
                if word_form_occurance < min_word_form_occurance:
                    min_word_form_occurance = word_form_occurance

            if min_word_form_occurance < 5:
                continue
            for word_form in word_forms:
                count = 0
                with open(dirpath + "/undersampling_data/" + word_form + ".tuple", 'r') as word_form_file:
                    lines = word_form_file.readlines()
                    while count < min_word_form_occurance:
                        line = lines.pop(random.randrange(len(lines)))
                        print(line)
                        train_tuple_file.write(line)
                        count += 1

        logging.info("Underampling: Finished removing samples")
