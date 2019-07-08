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
        Get the content of line given as second parameter
         of the file in the first parameter in a cleaned shape.
         Increase the line_counts by one of the given file_path
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
            raise ImportError('Input Files have not same number of lines. Stopping program execution')
        return line_contents

    def close_files_until(self, length):
        for i in range(length):
            self.file_contents[i].close()
