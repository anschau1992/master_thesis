import unittest
import os
from src.moses_file_reader import MosesFileReader


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
        print(os.path.dirname(__file__))
        self.assertRaises(Exception, MosesFileReader, [os.path.dirname(__file__) + '/test_file.en'])

    def test_wrong_file_path(self):
        """
        Initialize class without file_paths throws an error.
        :return:
        """
        self.assertRaises(SystemExit, MosesFileReader, [ os.path.dirname(__file__) + '/test_not_existing.en',
                                                         os.path.dirname(__file__) + '/test_file.de'])

    def test_not_equal_line_numbers(self):
        """
        Providing files with different number of lines will raise an Error, when reached
        :return: ImportError
        """
        moses_file_reader = MosesFileReader([os.path.dirname(__file__) + '/test_wrong_length.en',
                                             os.path.dirname(__file__) + '/test_file.de'])

        for i in range(0, 10):
            moses_file_reader.read_next_lines()

        self.assertRaises(Exception, moses_file_reader.read_next_lines)

    def test_first_line(self):
        """
        Function returns the first line of all files provided.
        :return:
        """
        moses_file_reader = MosesFileReader([os.path.dirname(__file__) + '/test_file.en',
                                             os.path.dirname(__file__) + '/test_file.de'])

        first_lines = moses_file_reader.read_next_lines()

        self.assertEqual(first_lines[0], 'Chat Logs')
        self.assertEqual(first_lines[1], 'Chat-Protokolle')
        moses_file_reader.close_files_until(2)

    def test_conditional_stop(self):
        """
        A while-loop over read_next_lines terminates after reaching the end of file-lines.
        :return:
        """
        moses_file_reader = MosesFileReader([os.path.dirname(__file__) + '/test_file.en',
                                             os.path.dirname(__file__) + '/test_file.de'])
        line_count = 0

        next_lines = moses_file_reader.read_next_lines()
        while next_lines:
            next_lines = moses_file_reader.read_next_lines()
            line_count += 1
        self.assertEqual(line_count, 20, 'Line count reaches 20 as both files have 20 lines')
