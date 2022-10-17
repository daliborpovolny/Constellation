import unittest
from main import *
from formulas import *


class TestMain(unittest.TestCase):

    def test_get_orbital_period(self):
        self.assertAlmostEqual(get_orb_period(600000 +  planets["earth"]["diameter"]/2 * 1000 , "earth"), 5792, -2)
        self.assertAlmostEqual(get_orb_period(150000 +  planets["earth"]["diameter"]/2 * 1000 , "earth"), 5241, -2)
        self.assertAlmostEqual(get_orb_period(450000000 +  planets["earth"]["diameter"]/2 * 1000 , "earth"), 3068292, -2)
        self.assertAlmostEqual(get_orb_period(400000 +  planets["earth"]["diameter"]/2 * 1000 , "earth"), 5545, -2)

if __name__ == '__main__':
    unittest.main()