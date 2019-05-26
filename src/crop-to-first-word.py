with open('../data/test.trg.de.output', 'r') as input_file:
    with open('../data/test.trg.de.output_one_word', 'w+') as output_file:
        for line in input_file:
            output_file.write(line.split(' ', 1)[0] + '\n')