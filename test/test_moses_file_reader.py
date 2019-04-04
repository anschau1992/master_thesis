import unittest
from src.moses_file_reader import read_moses_files
from src.config import TRAIN_TARGET_FILE_DE, RESULT_FILE_DE

resultPath_t = "./test_result" + RESULT_FILE_DE
targetPath_t = "./test_training" + TRAIN_TARGET_FILE_DE
differentLengthPath = "./test_length" + RESULT_FILE_DE


class TestMosesFileReader(unittest.TestCase):

    def test_not_list_param(self):
        """
        Throws exception when provided param is not a list
        :return:
        """
        self.assertRaises(Exception, read_moses_files, resultPath_t)

    def test_empty_list(self):
        """
        Throws exception when list is empty
        :return:
        """
        self.assertRaises(Exception, read_moses_files, [])

    def test_length_one_list(self):
        """
        Throws exception when list has length of one.
        :return:
        """
        self.assertRaises(Exception, read_moses_files, ['testPath'])

    def test_not_existing_path(self):
        """
        Throws an exception if one of the files provided do not exist.
        :return:
        """
        self.assertRaises(Exception, read_moses_files, [resultPath_t, './wrongPath'])

    def test_different_line_numbers(self):
        """
        Throws exception if the files provided have different number of lines
        -> Moses restricts different number of lines.
        :return:
        """
        self.assertRaises(Exception, read_moses_files, [differentLengthPath, targetPath_t])

    def test_returns_file_contents(self):
        """
        Function returns for each file a list.
        Each entry is a line entry of the corresponding file
        :return: list of two lists with string entries.
        """
        fileLists = read_moses_files([resultPath_t, targetPath_t])
        self.assertEqual(fileLists, [
            ['erweiterten', 'Rechte', 'Symbolisch', 'Verzeichnis', 'führen'],
            ['erweiterten', 'Rechte', 'Symbolischen', 'Verzeichnisse', 'führende']
        ])

    def test_mulptiple_inputs(self):
        """
        Function works also when there is more then two lists as input.
        :return:  list of three lists with string entries.
        """
        fileLists = read_moses_files([resultPath_t, targetPath_t, resultPath_t])
        self.assertEqual(fileLists, [
            ['erweiterten', 'Rechte', 'Symbolisch', 'Verzeichnis', 'führen'],
            ['erweiterten', 'Rechte', 'Symbolischen', 'Verzeichnisse', 'führende'],
            ['erweiterten', 'Rechte', 'Symbolisch', 'Verzeichnis', 'führen'],
        ])
