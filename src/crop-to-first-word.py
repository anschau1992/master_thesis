def __assure_line_break(line):
    if not '\n' in line:
        return line + '\n'
    return line


with open('../data/test.trg.de.output', 'r') as input_file:
    with open('../data/test.trg.de.output_one_word', 'w+') as output_file:
        for line in input_file:
            output_file.write(__assure_line_break(line.split(' ', 1)[0]))
