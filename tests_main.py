import unittest
from main import *
from formulas import *


class TestMain(unittest.TestCase):

    def test_get_orbital_period(self):
        self.assertAlmostEqual(get_orb_period(600000, "earth"), 5792)
        self.assertAlmostEqual(get_orb_period(150000, "earth"), 5241)
        self.assertAlmostEqual(get_orb_period(450000000, "earth"), 3068292)
        self.assertAlmostEqual(get_orb_period(400000, "earth"), 5545)

if __name__ == '__main__':
    unittest.main()