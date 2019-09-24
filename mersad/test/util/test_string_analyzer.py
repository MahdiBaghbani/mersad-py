# Python Standard Library
import unittest

from mersad.util import string_analyzer


class TestLetterIndexMapper(unittest.TestCase):
    def test_short_string(self):
        index = string_analyzer.map_letters_to_indexes(
                "Hi Martin, I think my TextAnalyzer is working!"
        )
        expected_result = {'!': [45], 'z': [31], 'o': [39], 'h': [14], 'y': [20, 30],
                           'w': [38], ' ': [2, 10, 12, 18, 21, 34, 37], 's': [36],
                           'i': [1, 7, 15, 35, 42], 'm': [19], 'A': [26], 'H': [0],
                           't': [6, 13, 25], 'T': [22], 'I': [11], 'a': [4, 28],
                           'k': [17, 41], 'e': [23, 32], 'n': [8, 16, 27, 43],
                           'g': [44], 'x': [24], 'r': [5, 33, 40], ',': [9],
                           'M': [3], 'l': [29]}
        self.assertEqual(expected_result, index)


class TestLetterIndexFinder(unittest.TestCase):
    def test_short_string(self):
        index = string_analyzer.find_letter_indexes(
                "Enumerate is an amazing Python function.", "a"
        )
        expected_result = [6, 13, 16, 18]
        self.assertEqual(expected_result, index)


if __name__ == '__main__':
    unittest.main()
