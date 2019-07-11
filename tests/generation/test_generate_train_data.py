import unittest
from src.generation.generator import generate_train_data_by_lines, generate_train_data


class TestGenerateTrainData(unittest.TestCase):

    def test_empty_string_parameter(self):
        """
        Empty strings should return empty lists back
        :return:
        """
        sources_en, sources_de, targets_de, bases_de = generate_train_data('', '')

        self.assertEqual(len(sources_en), 0, '"sources_en" has lenght of 0.')
        self.assertEqual(len(sources_de), 0, '"sources_de" has lenght of 0.')
        self.assertEqual(len(targets_de), 0, '"targets_de" has lenght of 0.')
        self.assertEqual(len(bases_de), 0, '"bases_de" has lenght of 0.')

    def test_whitespace_parameter(self):
        """
        Only withespace in strings should return empty lists back
        :return:
        """
        sources_en, sources_de, targets_de, bases_de = generate_train_data(' ', ' ')

        self.assertEqual(len(sources_en), 0, '"sources_en" has lenght of 0.')
        self.assertEqual(len(sources_de), 0, '"sources_de" has lenght of 0.')
        self.assertEqual(len(targets_de), 0, '"targets_de" has lenght of 0.')
        self.assertEqual(len(bases_de), 0, '"bases_de" has lenght of 0.')

    def test_not_string_param(self):
        """
        Raise an Exception, if one of the parameter is not a string
        :return:
        """
        self.assertRaises(Exception, generate_train_data, 'test string', 3)
        self.assertRaises(Exception, generate_train_data, 3, 'test string')

    def test_generation_of_train_data(self):
        """
        Checks if the returning values have all the length as expected.
        :return:
        """
        sources_en, sources_de, targets_de, bases_de = generate_train_data(
            'Record file and application usage',
            'Die Nutzung von Dateien und Anwendungen aufzeichnen')

        self.assertEqual(len(sources_en), 7, '"sources_en" has lenght of 7.')
        self.assertEqual(len(sources_de), 7, '"sources_de" has lenght of 7.')
        self.assertEqual(len(targets_de), 7, '"targets_de" has lenght of 7.')
        self.assertEqual(len(bases_de), 7, '"bases_de" has lenght of 7.')

    def test_unequal_token_length(self):
        """
        The lines of test data produces must match the number of tokens generated from the german sentence,
        even if the
        :return:
        """
        sources_en, sources_de, targets_de, bases_de = generate_train_data(
            'test short translation',
            'Dieser Schlüssel legt fest, ob die Karten per Ziehen-und-Ablegen oder per Anklicken gelegt werden sollen.')

        self.assertEqual(len(sources_en), 15, '"sources_en" has lenght of 15.')
        self.assertEqual(len(sources_de), 15, '"sources_de" has lenght of 15.')
        self.assertEqual(len(targets_de), 15, '"targets_de" has lenght of 15.')
        self.assertEqual(len(bases_de), 15, '"bases_de" has lenght of 15.')

    def test_source_en_contains_en(self):
        """
        The source_en return actually all the whole english sentence.
        :return:
        """
        sources_en, sources_de, targets_de, bases_de = generate_train_data(
            'Record file and application usage',
            'Die Nutzung von Dateien und Anwendungen aufzeichnen')
        for source_en in sources_en:
            self.assertEqual(source_en, 'Record file and application usage\n')

    def test_bases_de_contains_de(self):
        """
        The base_de return actually the whole german sentence.
        :return:
        """
        sources_en, sources_de, targets_de, bases_de = generate_train_data(
            'Record file and application usage',
            'Die Nutzung von Dateien und Anwendungen aufzeichnen')
        for base_de in bases_de:
            self.assertEqual(base_de, 'Die Nutzung von Dateien und Anwendungen aufzeichnen\n')

    def test_sources_de_contains_de(self):
        """
        The sources_de contains one token as the base form
         of the corresponding word of the whole sentence at each position.
        :return:
        """
        sources_en, sources_de, targets_de, bases_de = generate_train_data(
            'Record file and application usage',
            'Die Nutzung von Dateien und Anwendungen aufzeichnen')

        de_tokens = [
            'der\n',
            'Nutzung\n',
            'von\n',
            'Datei\n',
            'und\n',
            'Anwendung\n',
            'aufzeichnen\n'
        ]
        for i in range(0, len(sources_de)):
            self.assertEqual(sources_de[i], de_tokens[i],
                             'source_de entry: "{0}" matches with token "{1}" at position {2}'
                             .format(sources_de[i], de_tokens[i], i))

    def test_targets_de_contains_de(self):
        """
        The targets_de contains the actual german token inflected in their original form. at each position
        :return:
        """
        sources_en, sources_de, targets_de, bases_de = generate_train_data(
            'Record file and application usage',
            'Die Nutzung von Dateien und Anwendungen aufzeichnen')

        targets_tokens = ['Die\n',
                          'Nutzung\n',
                          'von\n',
                          'Dateien\n',
                          'und\n',
                          'Anwendungen\n',
                          'aufzeichnen\n'
                          ]

        for i in range(0, len(targets_de)):
            self.assertEqual(targets_de[i], targets_tokens[i],
                             'targets_de entry: "{0}" matches with token "{1}" at position {2}'
                             .format(targets_de[i], targets_tokens[i], i))
