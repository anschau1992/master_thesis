import random
import os
import logging


def oversample_data(source_file_en, source_file_de, target_file_de, base_file_de, pos_file_de, dirpath):
    logging.info("Start oversampling.")
    if not os.path.exists(dirpath + "/oversampling_data"):
        os.mkdir(dirpath + "/oversampling_data")

    #  TUPLE FILE CREATION
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

            train_tuple_file.write(source_en_line + "#" + source_de_line + "#"
                                   + target_de_line + "#" + base_de_line + "#"
                                   + pos_de_line + "\n")

            if source_de_line not in baseword_dicts:
                baseword_dicts[source_de_line] = {target_de_line}
            else:
                baseword_dicts[source_de_line].add(target_de_line)

            with open(dirpath + "/oversampling_data/" + target_de_line + ".tuple", 'a+') as target_tuple_file:
                target_tuple_file.write(source_en_line + "#" + source_de_line + "#"
                                        + target_de_line + "#" + base_de_line + "#"
                                        + pos_de_line + "\n")

        logging.info("Oversampling: Wrote all already existing line into tuple-file as tuples")

        for baseword_dict in baseword_dicts:
            word_forms = baseword_dicts[baseword_dict]
            max_word_form_occurance = 0
            line_counts = {}
            for word_form in word_forms:

                word_form_occurance = 0
                with open(dirpath + "/oversampling_data/" + word_form + ".tuple", 'r') as word_form_file:
                    for line in word_form_file:
                        word_form_occurance += 1
                line_counts[word_form] = word_form_occurance
                if word_form_occurance > max_word_form_occurance:
                    max_word_form_occurance = word_form_occurance

            for word_form in line_counts:
                upcount = line_counts[word_form]
                with open(dirpath + "/oversampling_data/" + word_form + ".tuple", 'r') as word_form_file:
                    lines = word_form_file.readlines()
                    while upcount < max_word_form_occurance:
                        train_tuple_file.write(random.choice(lines))
                        upcount += 1

        logging.info("Oversampling: Finished generating additional samples")
