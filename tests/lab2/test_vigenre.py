import unittest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class TestVigenreCipher(unittest.TestCase):

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



