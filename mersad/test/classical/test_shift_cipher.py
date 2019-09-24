# Python Standard Library
import os
import string
import unittest

# 3rd Party Library
from ErfanIO import ReaderIO  # type: ignore

# Mersad Library
from mersad.classical.shift_cipher import ShiftCipher


class TestBasics(unittest.TestCase):
    def setUp(self) -> None:
        self.ShiftCipher = ShiftCipher(key=3)

    def test_encrypt(self):
        self.assertEqual("Phuvdg", self.ShiftCipher.encrypt("Mersad"))

    def test_decrypt(self):
        self.assertEqual("Mersad", self.ShiftCipher.decrypt("Phuvdg"))

    def test_config(self):
        self.ShiftCipher.config(shuffle=True, seed=23, decrypt=True)
        self.assertEqual(3, self.ShiftCipher.configuration["key"])
        self.assertEqual(string.printable, self.ShiftCipher.configuration["letter_sequence"])
        self.assertEqual(23, self.ShiftCipher.configuration["seed"])
        self.assertEqual(True, self.ShiftCipher.configuration["shuffle"])
        self.assertEqual(True, self.ShiftCipher.configuration["decrypt"])

    def test_config_reset(self):
        self.ShiftCipher.config(shuffle=True, seed=23, decrypt=True)
        self.ShiftCipher.reset()
        self.assertEqual(0, self.ShiftCipher.configuration["key"])
        self.assertEqual(string.printable, self.ShiftCipher.configuration["letter_sequence"])
        self.assertEqual(False, self.ShiftCipher.configuration["shuffle"])
        self.assertEqual(0, self.ShiftCipher.configuration["seed"])
        self.assertEqual(False, self.ShiftCipher.configuration["decrypt"])

    def test_config_bad_type(self):
        with self.assertRaises(TypeError):
            self.ShiftCipher.config(letter_sequence=12)

        with self.assertRaises(TypeError):
            self.ShiftCipher.config(key="Hello There!")

        with self.assertRaises(TypeError):
            self.ShiftCipher.config(seed=True)

        with self.assertRaises(TypeError):
            self.ShiftCipher.config(shuffle=2)

        with self.assertRaises(TypeError):
            self.ShiftCipher.config(decrypt="False")


class TestEncryption(unittest.TestCase):
    def setUp(self) -> None:
        self.ShiftCipher = ShiftCipher()
        self.base_path = os.path.dirname(__file__).replace("mersad/test/classical", "mersad/test/asset/texts")
        self.plain_text = ReaderIO.reader(os.path.join(self.base_path, "Long License File.txt"), "text")

    def test_encrypt_without_shuffle(self):
        expected_cipher_text = ReaderIO.reader(os.path.join(self.base_path, "ShiftCipher-LLF-k25-sh0-s0.txt"), "text")
        self.ShiftCipher.config(key=25, shuffle=False, seed=0)
        self.assertEqual(expected_cipher_text, self.ShiftCipher.encrypt(self.plain_text))


if __name__ == '__main__':
    unittest.main()
