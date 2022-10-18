import unittest
from main import *
from formulas import *


class TestMain(unittest.TestCase):

    def test_get_orbital_period(self):
        self.assertAlmostEqual(get_orb_period(600000 +  planets["earth"]["radius"] , "earth"), 5801, None, None, 100)
        self.assertAlmostEqual(get_orb_period(450000000 +  planets["earth"]["radius"] , "earth"), 3068302.68, None, None, 1000)
        self.assertAlmostEqual(get_orb_period(400000 +  planets["earth"]["radius"] , "earth"), 5553.63, None, None, 100)

    def test_get_semimajor_axis(self):
        self.assertEqual(round(get_semimajor_axis(5802.289, "earth") -  planets["earth"]["radius"], -2),600000)
        self.assertEqual(round(get_semimajor_axis(3068302.68, "earth") -  planets["earth"]["radius"] , -7),450000000, None)
        self.assertEqual(round(get_semimajor_axis(5553.63, "earth") -  planets["earth"]["radius"] , -4),400000)

if __name__ == '__main__':
    unittest.main()