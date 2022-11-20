import unittest
from main import *
from formulas import *

def is_within_diff(value, desired_value, diff_by_percantage_of_desired_value): #diff must be: 0 -> 1
    real_difference = abs(desired_value - value)
    max_difference = value * diff_by_percantage_of_desired_value

    if real_difference <= max_difference:
        return True
    else:
        print(f"W max diff {max_difference} real diff {real_difference}")
        return False


class TestMain(unittest.TestCase):
 
    def test_get_orbital_period(self):
        self.assertAlmostEqual(get_orb_period(600000 +  planets["earth"]["radius"] , "earth"), 5801, None, None, 100)
        self.assertAlmostEqual(get_orb_period(450000000 +  planets["earth"]["radius"] , "earth"), 3068302.68, None, None, 1000)
        self.assertAlmostEqual(get_orb_period(400000 +  planets["earth"]["radius"] , "earth"), 5553.63, None, None, 100)

    def test_get_semimajor_axis(self):
        self.assertEqual(round(get_semimajor_axis(5802.289, "earth") -  planets["earth"]["radius"], -2),600000)
        self.assertEqual(round(get_semimajor_axis(3068302.68, "earth") -  planets["earth"]["radius"] , -7),450000000, None)
        self.assertEqual(round(get_semimajor_axis(5553.63, "earth") -  planets["earth"]["radius"] , -4),400000)
    
    def test_get_transfer_orbit_mode_dive(self):
        self.assertTrue(is_within_diff(get_transfer_orb(10000000, 4, 2, "earth", True)[1], 4285925.5, 0.01))
        self.assertTrue(is_within_diff(get_transfer_orb(8000000, 8, 2, "mars", True)[1], 6062164.9, 0.01))
        self.assertTrue(is_within_diff(get_transfer_orb(2439700, 3, 2, "mercury", True)[1], 128258.2, 0.01))
        self.assertTrue(is_within_diff(get_transfer_orb(6049000, 3, 2, "venus", True)[1], 318003.9, 0.01))

    def test_dv_required_for_ciculalization(self):
        self.assertTrue(is_within_diff(get_transfer_orb(10000000, 4, 2, "earth", True)[2], 552.53, 0.1))
        self.assertTrue(is_within_diff(get_transfer_orb(10000000, 4, 3, "earth", True)[2], 329.99, 0.1))

if __name__ == '__main__':
    unittest.main()
