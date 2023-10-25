import unittest
import sys
sys.path.append('/Users/viktorivanov/cs102/src/lab2')

from rsa import is_prime, gcd, multiplicative_inverse, encrypt, decrypt


class TestRsaCipher(unittest.TestCase):

    def test_is_prime_rsa(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(8), False)

    def test_gcd_rsa(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)

    def test_multiplicative_inverse_rsa(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)


