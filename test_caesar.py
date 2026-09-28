import unittest

from caesar import decrypt, encrypt


class TestCaesar(unittest.TestCase):
    def test_encrypt_basic(self):
        self.assertEqual(encrypt("abc", 3), "def")

    def test_wraps_around_alphabet(self):
        self.assertEqual(encrypt("xyz", 3), "abc")

    def test_keeps_case_and_punctuation(self):
        self.assertEqual(encrypt("Hello, World!", 3), "Khoor, Zruog!")

    def test_decrypt_reverses_encrypt(self):
        message = "Attack at dawn!"
        self.assertEqual(decrypt(encrypt(message, 7), 7), message)

    def test_large_and_negative_shifts(self):
        self.assertEqual(encrypt("abc", 29), "def")
        self.assertEqual(encrypt("def", -3), "abc")


if __name__ == "__main__":
    unittest.main()
