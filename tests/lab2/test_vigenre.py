import unittest
import sys
sys.path.append('/Users/viktorivanov/cs102/src/lab2')

from vigenre import encrypt_vigenere, decrypt_vigenere

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_vigenre(self):
        self.assertEqual(encrypt_vigenere("VIKTOR", "A"), 'VIKTOR')
        self.assertEqual(encrypt_vigenere("viktor", 'a'), 'viktor')
        self.assertEqual(encrypt_vigenere("VIKTORLIKEBEER", "FISH"), 'AQCATZDPPMTLJZ')

    def test_decrypt_vigenre(self):
        self.assertEqual(decrypt_vigenere("VIKTOR", 'A'), 'VIKTOR')
        self.assertEqual(decrypt_vigenere("viktor", 'a'), 'viktor')
        self.assertEqual(decrypt_vigenere("AQCATZDPPMTLJZ", "FISH"), 'VIKTORLIKEBEER')

if __name__ == '__main__':
    unittest.main()



