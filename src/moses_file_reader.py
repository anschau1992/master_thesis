import logging
import sys


class MosesFileReader:

    def __init__(self, file_paths):
        if len(file_paths) < 2:
            logging.info('MosesFileReader: There must be at least two file paths')
            raise Exception('MosesFileReader: There must be at least two file paths')

        self.file_contents = []
        for i in range(len(file_paths)):
            try:
                self.file_contents.append(open(file_paths[i]))
            except IOError or FileNotFoundError as e:
                self.close_files_until(i)
                logging.info('MosesFileReader: ' + str(e))
                logging.info('Stopping program execution')
                sys.exit('MosesFileReader: ' + str(e))

        self.files_numb = len(self.file_contents)

    def read_next_lines(self):
        """
        Get the content of the next line of all the different files defined in prior in the constructor.
        :param file_path:
        :param line_number:
        :return: line content, cleaned
        """
        line_contents = []
        for i in range(0, self.files_numb):
            line = self.file_contents[i].readline()
            if line:
                line_contents.append(line.rstrip())
        if len(line_contents) == 0:
            self.close_files_until(len(self.file_contents))
            return None
        elif len(line_contents) != self.files_numb:
            logging.info('Input Files have not same number of lines. Stopping program execution')
            self.close_files_until(len(self.file_contents))
            raise Exception('Input Files have not same number of lines. Stopping program execution')
        return line_contents

    def close_files_until(self, length):
        if length is None:
            length = len(self.file_contents)
        for i in range(length):
            self.file_contents[i].close()


def read_moses_files(file_paths: list):
    """
    Opens files provided as parameter. It reads in line by line
    and returns all content.
    It also checks for same line length of each file,
    as the position are treated as pairs afterwards.

    :param file_paths:
    :return: a list of lists.
     The size of the first list correspond on the size of file-paths given as argument.
    """
    logging.info('Moses_file_reader: Starting')

    if len(file_paths) <= 1:
        ex_msg = 'Passed param must at least have length of 2'
        logging.exception(ex_msg)
        raise Exception(ex_msg)

    is_line_numb_defined = False
    line_number = 0
    files_contents = []

    for fp in file_paths:
        with open(fp, 'r') as file:
            file_content = file.readlines()

            if not is_line_numb_defined:
                line_number = len(file_content)
                is_line_numb_defined = True

            if line_number != len(file_content):
                ex_msg = 'File line numbers are not equal'
                logging.exception(ex_msg)
                raise Exception(ex_msg)

            file_content = __strip_line_breaks(file_content)
            files_contents.append(file_content)

    logging.info('Moses_file_reader: Success')
    return files_contents


def __strip_line_breaks(tex_list: list):
    new_tl_list = []
    for tl in tex_list:
        new_tl_list.append(tl.rstrip())
    return new_tl_list
