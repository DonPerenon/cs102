import unittest
import sys
sys.path.append('../../src/lab2')

from caesar import encrypt_caesar, decrypt_caesar


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar("HELLO"), 'KHOOR')
        self.assertEqual(encrypt_caesar("caesar"), 'fdhvdu')
        self.assertEqual(encrypt_caesar("Cipher1000-7"), 'Flskhu1000-7')
        self.assertEqual(encrypt_caesar(""), '')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar("KHOOR"), 'HELLO')
        self.assertEqual(decrypt_caesar("fdhvdu"), 'caesar')
        self.assertEqual(decrypt_caesar("Flskhu1000-7"), 'Cipher1000-7')
        self.assertEqual(decrypt_caesar(""), '')

if __name__ == '__main__':
    unittest.main()
