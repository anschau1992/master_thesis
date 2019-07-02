import unittest
from src.moses_file_reader import MosesFileReader
from src.config import TRAIN_TARGET_FILE_DE, RESULT_FILE_DE

resultPath_t = "./test_result" + RESULT_FILE_DE
targetPath_t = "./test_training" + TRAIN_TARGET_FILE_DE
differentLengthPath = "./test_length" + RESULT_FILE_DE


class TestMosesFileReader(unittest.TestCase):

    def test_no_file_path(self):
        """
        Initilaize the class without any file_pats throws an exception
        :return: e
        """
        self.assertRaises(Exception, MosesFileReader, [])

    def test_not_enough_file_paths(self):
        """
        Initialize class without enough file_paths throws an error
        :return:
        """
        self.assertRaises(Exception, MosesFileReader, ['./test_file.en'])

    def test_wrong_file_path(self):
        """
        Initialize class without file_paths throws an error.
        :return:
        """
        self.assertRaises(SystemExit, MosesFileReader, ['./test_not_existing.en', './test_file.de'])

    def test_not_equal_line_numbers(self):
        """
        Providing files with different number of lines will raise an Error, when reached
        :return: ImportError
        """
        moses_file_reader = MosesFileReader(['./test_wrong_length.en', './test_file.de'])

        for i in range(0, 10):
            moses_file_reader.read_next_lines()

        self.assertRaises(ImportError, moses_file_reader.read_next_lines)

    def test_first_line(self):
        """
        Function returns the first line of all files provided.
        :return:
        """
        moses_file_reader = MosesFileReader(['./test_file.en', './test_file.de'])

        first_lines = moses_file_reader.read_next_lines()

        self.assertEqual(first_lines[0], 'Chat Logs')
        self.assertEqual(first_lines[1], 'Chat-Protokolle')
        moses_file_reader.close_files_until(2)

    def test_conditional_stop(self):
        """
        A while-loop over read_next_lines terminates after reaching the end of file-lines.
        :return:
        """
        moses_file_reader = MosesFileReader(['./test_file.en', './test_file.de'])
        line_count = 0

        next_lines = moses_file_reader.read_next_lines()
        while next_lines:
            next_lines = moses_file_reader.read_next_lines()
            line_count += 1
        self.assertEqual(line_count, 20, 'Line count reaches 20 as both files have 20 lines')
