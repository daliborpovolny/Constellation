import unittest
from main import *
from formulas import *

def is_within_diff(value, desired_value, diff_by_percantage_of_desired_value): #diff must be: 0 -> 1
    real_difference = abs(desired_value - value)
    print(value, desired_value)
    if ((value < desired_value) and (value + desired_value*diff_by_percantage_of_desired_value >= desired_value)) or ((value > desired_value) and (value + desired_value*diff_by_percantage_of_desired_value <= desired_value)):
        print(f"OKAY, max allowed difference is {desired_value*diff_by_percantage_of_desired_value}, real difference is {real_difference}")
        return True
    elif value == desired_value:
        print(f"value completely same")
        return True
    else:
        print(f"WRONG, max allowed difference is {desired_value*diff_by_percantage_of_desired_value}, real difference is {real_difference}")
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
    
    # def test_new_test_function(self):
    #     self.assertTrue(is_within_diff(10,10,0.10))
    #     self.assertTrue(is_within_diff(10,20,0.50))

    def test_get_transfer_orbit_mode_dive(self):
        self.assertTrue(is_within_diff(get_transfer_orb(10000000, 4, 2, "earth")[1], 4285925.5, 0.01))
        self.assertTrue(is_within_diff(get_transfer_orb(8000000, 8, 2, "mars")[1], 6062164.9, 0.01))
        self.assertTrue(is_within_diff(get_transfer_orb(2439700, 3, 2, "mercury")[1], 128258.2, 0.01))
        self.assertTrue(is_within_diff(get_transfer_orb(6049000, 3, 2, "venus")[1], 318003.9, 0.01))


if __name__ == '__main__':
    unittest.main() 
